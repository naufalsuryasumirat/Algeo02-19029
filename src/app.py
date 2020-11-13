import os
from flask import Flask, request, render_template, url_for, redirect, flash, send_from_directory
from flask_sqlalchemy import SQLAlchemy
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

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Hasil searching dalam bentuk list of dictionary sebagai global variable
search_result = []
# List dokumen yang berada pada folder upload
files = get_listsemuadokumen()
# Query user sebagai global variable untuk digunakan oleh fungsi-fungsi lain
query = ""

## HOME PAGE
@app.route('/')
def home():
    return render_template('homepage.html')

## HOME PAGE
@app.route('/', methods = ['GET', 'POST'])
def search_text():
    if request.method == "POST":
        global query, search_result
        query = ""
        query += request.form['query']
        ## Cek jika input query valid atau tidak
        ## Jika hanya mengandung stop words maka tidak valid
        ## Jika hanya spasi tidak valid
        if len(get_query(query)) == 0:
            return render_template('homepage.html')
        else :
            return redirect("/search")
    return render_template('homepage.html')

# Page redirect setelah mengetikkan query pada home page
@app.route('/search', methods = ['GET', 'POST'])
def searching():
    global query, search_result, files
    search_result = scrape_local(query)
    return render_template('search.html', search_result = search_result)

## File yang telah diupload untuk diakses nantinya
### Cotntoh /uploaded/1.html jika upload 1.html
@app.route('/uploaded/<filename>')
def view_upload(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# localhost:5000/upload
## Untuk upload file dengan sistem secure file extension (hanya bisa upload .html)
@app.route('/upload', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Memeriksa jika Request POST memiliki bagian file
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        # Handle jika user belum memilih file namun sudah meng-klik upload
        if file.filename == '':
            return render_template('upload2.html')
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file', filename=filename))
    return render_template('upload2.html')

# localhost:5000/tabel
## Untuk melihat tabel hasil query dibandingkan dengan semua dokumen
@app.route('/tabel', methods = ['GET'])
def tabel():
    global search_result, query
    return render_template('tabel.html', search_result = search_result)

# localhost:5000/upload
## Untuk upload file
@app.route('/upload')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# localhost:5000/about
## About us page
@app.route('/about')
def aboutus():
    return render_template('about.html')

# debug mode untuk mempermudah bug fixing dan modifikasi
if __name__ == "__main__":
    app.run(debug = True)