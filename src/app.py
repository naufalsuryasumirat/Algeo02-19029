import os
from flask import Flask, request, render_template, url_for, redirect, flash, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_dropzone import Dropzone
from scraping import *
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage

## Menjalankan proses scrape
#scrape()

# Extention yang diperbolehkan untuk upload
ALLOWED_EXTENSIONS = {'html'}

app = Flask(__name__)
# APP_ROOT merupakan directory file ini dalam absolute path
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
# Directory tempat penyimpanan hasil upload user
UPLOAD_FOLDER = os.path.join(APP_ROOT, 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

dropzone = Dropzone(app)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Hasil searching dalam bentuk list of dictionary sebagai global variable
search_result = []
# List dokumen yang berada pada folder uploads
files = get_listsemuadokumen()
# Query user sebagai global variable untuk digunakan oleh fungsi-fungsi lain
query = ""
# Tabel untuk diperlihatkan di web (dalam bentuk list)
table = []

## HOME PAGE
@app.route('/')
def home():
    ## Mengupdate list files jika files di delete
    global files
    files = get_listsemuadokumen()
    return render_template('homepage.html', files = files)

## HOME PAGE
@app.route('/', methods = ['GET', 'POST'])
def search_text():
    ## Mengupdate list files jika files di delete
    global files
    files = get_listsemuadokumen()
    if request.method == "POST":
        global query, search_result
        query = ""
        query += request.form['query']
        ## Cek jika input query valid atau tidak
        ## Jika hanya mengandung stop words maka tidak valid
        ## Jika hanya spasi maka tidak valid
        if len(get_query(query)) == 0:
            return render_template('homepage.html', files = files)
        else :
            return redirect("/search")
    return render_template('homepage.html', files = files)

# Page redirect setelah mengetikkan query pada home page
@app.route('/search', methods = ['GET', 'POST'])
def searching():
    ## Mengupdate list files jika files di delete
    global query, search_result, files, table
    files = get_listsemuadokumen()
    search_result = scrape_local(query)
    table = get_table(query, search_result)
    if request.method == "POST":
        query2 = ""
        query2 += request.form['query']
        if len(get_query(query2)) == 0:
            return redirect(request.url)
        else:
            query = query2
            return redirect(request.url)
    return render_template('search.html', search_result = search_result, files = files)

## File yang telah diupload untuk diakses nantinya
### Contoh /uploaded/1.html jika upload 1.html
@app.route('/uploaded/<filename>')
def view_upload(filename):
    ## Mengupdate list files jika files di delete
    global files
    files = get_listsemuadokumen()
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# localhost:5000/upload
## Untuk upload file dengan sistem secure file extension (hanya bisa upload .html)
@app.route('/upload', methods = ['GET', 'POST'])
def upload_file():
    ## Mengupdate list files jika files di delete
    global files
    files = get_listsemuadokumen()
    if request.method == 'POST':
        uploaded = request.files.getlist("file[]")
        filenames = []
        ## Mengecek jika tidak ada file yang diupload tapi sudah memencet tombol upload tidak akan terjadi apa apa
        if uploaded[0].filename == '':
            return redirect(request.url)
        for file in uploaded:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                filenames.append(filename)
    return render_template('upload.html')

# localhost:5000/upload
## Untuk upload file
@app.route('/upload')
def uploaded_file(filename):
    ## Mengupdate list files jika files di delete
    global files
    files = get_listsemuadokumen()
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# localhost:5000/tabel
## Untuk melihat tabel hasil query dibandingkan dengan semua dokumen
@app.route('/tabel', methods = ['GET'])
def tabel():
    ## Mengupdate list files jika files di delete
    global search_result, query, table, files
    files = get_listsemuadokumen()
    return render_template('tabel.html', search_result = search_result, table = table)

# localhost:5000/about
## About us page
@app.route('/about')
def aboutus():
    ## Mengupdate list files jika files di delete
    global files
    files = get_listsemuadokumen()
    return render_template('about.html')

# localhost:5000/instructions
## How to use page
@app.route('/instructions')
def instructions():
    ## Mengupdate list files jika files di delete
    global files
    files = get_listsemuadokumen()
    return render_template('instructions.html')

# debug mode untuk mempermudah bug fixing dan modifikasi
if __name__ == "__main__":
    app.run(debug = True)