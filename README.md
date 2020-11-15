# Algeo02-19029
### 13519029 - Nicholas Chen
### 13519098 - Jordan Daniel Joshua
### 13519135 - Naufal Alexander Suryasumirat

![logo](https://github.com/naufalsuryasumirat/Algeo02-19029/blob/main/images/logo.jpg?raw=true)

## Table of contents
* [Library](#library)
* [Setup](#setup)
* [Screenshots](#screenshots)
* [LibraryGuide](#libraryguide)

## Library
List library yang digunakan:
1. Virtual Environment
2. NLTK
3. Sastrawi
4. Math
5. Beautiful Soup
6. Requests
7. Flask
8. lxml
9. Werkzeug

## Setup
### Tugas Besar ini menggunakan python3
1. Run Windows PowerShell as Administrator
2. Copy paste *Set-ExecutionPolicy Unrestricted -Force* pada Windows Powershell agar dapat menggunakan Virtual Environment
3. Install library Virtual Environment dengan menggunakan *pip3 install virtualenv*
4. Kemudian clone repo ini
5. Ganti directory pada file pyenv.cfg dalam folder Algeo dengan directory tempat install python.exe (Ganti "noler" dengan nama user pada windows yang digunakan atau ganti dengan directory ke python.exe)
6. Buka Folder hasil clone repository ini pada VSCode dan ketik *.\src\Algeo\Scripts\activate* dalam terminal VSCode
7. Pastikan Terminal VSCode berada pada directory dengan akhiran Algeo02-19029>
8. Jalankan app.py
9. Program akan melakukan proses scraping dan menyimpan hasilnya sebagai html pada folder test (sebelumnya ada 1 html file agar folder tidak di delete oleh github, setelah scraping akan terdapat 20 dokumen baru)
10. Buka web-browser localhost:5000
11. Pilih upload pada top bar home page untuk upload file hasil scraping
12. Instruksi lebih lanjut ada pada page localhost:5000/instructions (dapat diakses pada tombol instructions pada bagian atas home page)

app.py menggunakan scraping.py (menjalankan proses scraping dari https://bola.kompas.com/liga-inggris, sekaligus yang menghitung similaritas query dengan dokumen yang telah diupload)

Tiap library yang digunakan sudah terdapat dalam virtual environment Algeo dan dapat digunakan jika sudah menginstall virtualenv dan menuliskan .src\Algeo\Scripts\activate pada terminal VSCode lalu menjalankan app.py. Jika tidak bisa digunakan maka harus install list library di atas.

### Setup Library jika tidak dapat menggunakan Virtual Environment
1. NLTK (pip3 install nltk dan jalankan program nltkinstall.py)
2. Sastrawi (pip3 install Sastrawi)
3. Math
4. Beautiful Soup (pip3 install beautifulsoup4)
5. requests (pip3 install requests)
6. Flask (pip3 install Flask)
7. lxml (pip3 install lxml)
8. Werkzeug (pip3 install Werkzeug)

## Screenshots
![guide_1](https://github.com/naufalsuryasumirat/Algeo02-19029/blob/main/images/guide_1.jpg?raw=true)
![guide_12](https://github.com/naufalsuryasumirat/Algeo02-19029/blob/main/images/guide_12.jpg?raw=true)
![guide_2](https://github.com/naufalsuryasumirat/Algeo02-19029/blob/main/images/guide_2.jpg?raw=true)
![guide_3](https://github.com/naufalsuryasumirat/Algeo02-19029/blob/main/images/guide_3.jpg?raw=true)
![guide_4](https://github.com/naufalsuryasumirat/Algeo02-19029/blob/main/images/guide_4.jpg?raw=true)
![guide_5](https://github.com/naufalsuryasumirat/Algeo02-19029/blob/main/images/guide_5.jpg?raw=true)
![guide_6](https://github.com/naufalsuryasumirat/Algeo02-19029/blob/main/images/guide_6.jpg?raw=true)
![guide_7](https://github.com/naufalsuryasumirat/Algeo02-19029/blob/main/images/guide_7.jpg?raw=true)
![guide_8](https://github.com/naufalsuryasumirat/Algeo02-19029/blob/main/images/guide_8.jpg?raw=true)
![guide_9](https://github.com/naufalsuryasumirat/Algeo02-19029/blob/main/images/guide_9.jpg?raw=true)
![guide_10](https://github.com/naufalsuryasumirat/Algeo02-19029/blob/main/images/guide_10.jpg?raw=true)
![guide_11](https://github.com/naufalsuryasumirat/Algeo02-19029/blob/main/images/guide_11.jpg?raw=true)

## LibraryGuide
Khusus untuk NLTK harus menjalankan nltkinstall.py untuk menginstall package nltk (all packages)
![guide2_1](https://github.com/naufalsuryasumirat/Algeo02-19029/blob/main/images/guide2_1.jpg?raw=true)
![guide2_2](https://github.com/naufalsuryasumirat/Algeo02-19029/blob/main/images/guide2_2.jpg?raw=true)
![guide2_9](https://github.com/naufalsuryasumirat/Algeo02-19029/blob/main/images/guide2_9.jpg?raw=true)
![guide2_3](https://github.com/naufalsuryasumirat/Algeo02-19029/blob/main/images/guide2_3.jpg?raw=true)
![guide2_4](https://github.com/naufalsuryasumirat/Algeo02-19029/blob/main/images/guide2_4.jpg?raw=true)
![guide2_5](https://github.com/naufalsuryasumirat/Algeo02-19029/blob/main/images/guide2_5.jpg?raw=true)
![guide2_6](https://github.com/naufalsuryasumirat/Algeo02-19029/blob/main/images/guide2_6.jpg?raw=true)
![guide2_7](https://github.com/naufalsuryasumirat/Algeo02-19029/blob/main/images/guide2_7.jpg?raw=true)
![guide2_8](https://github.com/naufalsuryasumirat/Algeo02-19029/blob/main/images/guide2_8.jpg?raw=true)
