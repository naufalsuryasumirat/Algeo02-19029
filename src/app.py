import os
from flask import Flask, request, render_template, url_for, redirect, flash, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from scraping import *
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage

ALLOWED_EXTENSIONS = {'html'}

app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

## HOME PAGE
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('homepage.html')

## File yang telah diupload untuk diakses nantinya
@app.route('/uploaded/<filename>')
def view_upload(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Memeriksa jika Request POST memiliki bagian file
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # Handle jika user belum memilih file namun sudah meng-klik upload
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file', filename=filename))
    return render_template('upload2.html')

@app.route('/upload')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == "__main__":
    app.run(debug = True)