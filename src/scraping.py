import requests
import nltk
import string
import math
import os
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from os import listdir

def get_link(request):
# Mengambil semua link dari main-page kompas liga-inggris dan mengembalikannya dalam bentuk list
# request = "https://bola.kompas.com/liga-inggris"
# Hasil : ["link1", "link2", ...]
    result = requests.get(request)
    source = result.content
    soup = BeautifulSoup(source, 'lxml')
    List_link = []
    for h3_tag in soup.find_all("h3"):
        a_tag = h3_tag.find('a')
        List_link.append(a_tag.attrs['href'])
    # Mengembalikan list of link dari page "https://bola.kompas.com/liga-inggris"
    # Yang berisi link article-article yang akan digunakan
    return List_link

def print_list(List):
# Meng-output / print isi dari List
# Untuk men-check isi List
    for i in range(len(List)):
        print(List[i])

def add_link(List, string):
# Menambahkan "?page=all#page2" pada link agar memperlihatkan seluruh isi artikel berita (karena biasanya terbagi 2 halaman lebih)
# Hasil : ["link1" + string, "link2" + string, ...]
    for i in range(len(List)):
        List[i] += string

def get_document(List_link):
# Mengambil isi berita dari artikel dalam List_link dan mengembalikannya dalam bentuk list of string
# Hasil : ["dokumen1", "dokumen2", ...]
    List_document = []
    for link in range(len(List_link)):
        links = requests.get(List_link[link])
        src = links.content
        bsoup = BeautifulSoup(src, 'lxml')
        article_text = bsoup.find_all('div', class_ = 'read__content')
        string_teks = article_text[0].get_text()
        List_document.append(string_teks)
    return List_document

def get_title(List_link):
# Mengambil judul dari tiap artikel dan mengembalikannya dalam bentuk list of string yang berisi judul
# Hasil : ["judul1", "judul2", ...]
    List_title = []
    for link in range(len(List_link)):
        links = requests.get(List_link[link])
        src = links.content
        bsoup = BeautifulSoup(src, 'lxml')
        article_title = bsoup.find('h1', class_ = 'read__title')
        List_title.append(article_title.text.strip())
    return List_title

def get_firstsentence(List_document):
# Mengambil kalimat pertama dari semua dokumen dan mengembalikannya dalam bentuk list of string kalimat pertama
# Hasil : ["sentence1", "sentence3", ...]
    list_firstsentence = []
    for sentence in range (len(List_document)):
        document = List_document[sentence]
        first_sentence = nltk.tokenize.sent_tokenize(document)
        list_firstsentence.append(first_sentence[0])
    return list_firstsentence

def get_vectorwords(List_document):
# Mengambil dokumen dan menjadikan vektor kata-kata dalam dokumen
# Hasil : [[('kata1_doc1', jumlah), ...], [('kata1_doc2', jumlah), ...], ...]
    list_vectorwords = []
    stop_words = set(stopwords.words('indonesian'))

    # Pake stop_words
    not_in_stop_words = ["—", "’"]
    stop_words.update(not_in_stop_words)
    # Meng-update list kata stop_words untuk menghilangkan hal yang tidak diperlukan

    for document in range (len(List_document)):
        artikel = List_document[document].translate(str.maketrans('','',string.punctuation)).lower()
        tokenized_artikel = nltk.tokenize.word_tokenize(artikel)
        filtered_words = []
        for word in tokenized_artikel:
            if word not in stop_words:
                filtered_words.append(word)
        filtered_words = nltk.FreqDist(filtered_words)
        filtered_words = filtered_words.most_common()
        list_vectorwords.append(filtered_words)
    return list_vectorwords

def panjang_listvektor(List):
# Fungsi untuk menentukan panjang vektor
    panjang = 0
    for i in range (len(List)):
        panjang += List[i][1] * List[i][1]
    return math.sqrt(panjang)

def similarityList(LQuery, LDocument):
# Fungsi untuk menghitung similarity antara Query dengan Document
# Contoh Hasil : 0.94..
    dot_product = 0
    for i in range (len(LQuery)):
        for j in range(len(LDocument)):
            if (LQuery[i][0] == LDocument[j][0]):
                dot_product += (LQuery[i][1] * LDocument[j][1])
                # Jika sudah ditemukan kata yang sama maka akan di break dan lanjut ke kata berikutnya dalam query
                break
    # Rumus cosine similarity
    return (dot_product)/(panjang_listvektor(LQuery) * panjang_listvektor(LDocument))

def get_similarity(Query, List_processedwords):
# Menerima input Query yang telah diproses dan List dari hasil fungsi get_vectorwords
# Mengembalikan List berisi similarity antar Query dengan tiap dokumen
# Contoh hasil : [0.007, 0.98, ...]
    list_similarity = []
    for doc in range (len(List_processedwords)):
        sim = similarityList(Query, List_processedwords[doc])
        list_similarity.append(sim)
    return list_similarity

def get_banyakkata(List_processedwords):
# Menerima input List hasil get_vectorwords
# Mengembalikan banyak kata (yang sudah di hilangkan stopwords)
# Hasil list of integers
    jumlah = 0
    list_jumlah = []
    for i in range (len(List_processedwords)):
        for j in range (len(List_processedwords[i])):
            jumlah = jumlah + List_processedwords[i][j][1]
        list_jumlah.append(jumlah)
    return list_jumlah
## Fungsi belom dicek tolong dicek nanti

# TAMBAHIN QUERY DALEM FUNGSI INI
def get_allwordsfromalldocuments(List_document):
# Menerima input list dokumen yang telah diambil
# Memproses untuk mendapatkan semua kata dalam semua dokumen
# Mengembalikan dalam bentuk list of words
    all_words = ""
    stop_words = set(stopwords.words('indonesian'))

    # Pake stop_words
    not_in_stop_words = ["—", "’"]
    stop_words.update(not_in_stop_words)

    # — ’ ini karakternya aneh bet tambahin ke stopwords mungkin

    for i in range(len(List_document)):
        all_words += List_document[i]

    all_words = all_words.translate(str.maketrans('','',string.punctuation)).lower()
    tokenized_words = nltk.tokenize.word_tokenize(all_words)
    list_allwords = []
    for word in tokenized_words:
        if word not in stop_words:
            list_allwords.append(word)
    list_allwords = nltk.FreqDist(list_allwords)
    list_allwords = list_allwords.most_common()

    list_onlywords = []
    for onlyword in range(len(list_allwords)):
        list_onlywords.append(list_allwords[onlyword][0])

    list_onlywords = sorted(list_onlywords)
    return list_onlywords

def print_similarity(ListofDictionary_results):
# Untuk check jika similarity telah diurut
    for x in ListofDictionary_results:
        print(x['similarity'])
    
def toHTML(scrape_result):
    for scrape in range (len(scrape_result)):
        savedHTML = open("test/" + str(scrape + 1) + ".html", "w")
        toSave = "<html><head><title>"
        toSave += scrape_result[scrape].get("title")
        toSave += "</title></head><body><h1>"
        toSave += scrape_result[scrape].get("title")
        toSave += "</h1><p>"
        toSave += scrape_result[scrape].get("content")
        toSave += "</p></body></html>"
        savedHTML.write(toSave)
        savedHTML.close()

def scrape():
    # Fungsi untuk menjalankan proses scrape dan menuliskan dalam bentuk html ke folder test untuk diupload
    # list test query
    query = [('gol', 1), ('penalti', 1), ('kiper', 2), ('gawang', 2)] # Tidak digunakan dalam proses penentuan hasil searching pada web

    list_url = get_link("https://bola.kompas.com/liga-inggris")
    add_link(list_url, "?page=all#page2")

    ## print isi list_url dengan rapi
    #print_list(list_url)

    ## print isi array list_url
    #print(len(list_url))

    # List isi berita tiap artikel
    list_dokumen = get_document(list_url)
    #print_list(list_dokumen)

    # List judul tiap berita
    list_title = get_title(list_url)
    #print_list(list_title)
    
    # List kalimat utama tiap artikel
    list_sentence = get_firstsentence(list_dokumen)
    #print_list(list_sentence)

    # List kata-kata yang sudah diproses untuk dihitung similarity
    list_processedwords = get_vectorwords(list_dokumen)
    #print_list(list_processedwords)
    #print(list_processedwords)

    # List similarity query dengan tiap dokumen
    list_similarity = get_similarity(query, list_processedwords)
    #print_list(list_similarity)
    # Buat fungsi buat dapetin Query hitung dengan tiap dokumen, isi list_similarity

    # List jumlah kata
    list_jumlahkata = get_banyakkata(list_processedwords)
    # mungkin diganti fungsinya buat jumlah seluruh kata dengan stopwords

    # List semua kata pada semua dokumen dan query
    # BELOM DITAMBAH QUERY
    list_allwords = get_allwordsfromalldocuments(list_dokumen)
    #print(list_allwords)
    #print_list(list_allwords)
    #print(len(list_allwords))

    # Hasil search dalam bentuk list of dictionaries
    ## BUAT FUNGSI GET_SEARCHRESULTS?
    ## SORT BERDASARKAN VALUE SIMILARITY
    scraping_results = [{
                        "link"      : val[0], 
                        "title"     : val[1], 
                        "content"   : val[2], 
                        "words"     : val[3], # Tidak digunakan
                        "fsentence" : val[4], # Tidak digunakan
                        "similarity": val[5], # Tidak digunakan
                        "count"     : val[6]} # Tidak digunakan
                        for val in zip(list_url, list_title, list_dokumen, list_processedwords, list_sentence, list_similarity, list_jumlahkata)]

    # Memakai fungsi bawaan python untuk sort search_results berdasarkan similiarity
    # Similarity disini tidak berhubungan dengan input Query pengguna, hanya untuk scrape dokumen dari kompas.com
    scraping_results = sorted(scraping_results, key = lambda k: k['similarity'], reverse = True)

    toHTML(scraping_results)
    scraping_results = sorted(scraping_results, key = lambda k: k['similarity'], reverse = True)

    toHTML(scraping_results)

def get_link_local(path_to_uploads_folder):
# Menerima path ke folder uploads pada src/
# Mengirimkan path dengan tambahan semua nama file untuk dibuka dan diproses
# Bentuk input: path = os.path.dirname(os.path.abspath(__file__))
#               path_to_uploads = os.path.join(path, 'uploads')
# Hasil sebuah list berisi path seperti: [c:\\Users\\..., c:\\Users...] (List_directory)
    list_files = os.listdir(path_to_uploads_folder)
    list_directory = []
    for files in list_files:
        pathdir = os.path.join(path_to_uploads_folder, str(files))
        list_directory.append(pathdir)
    return list_directory

def get_title_local(List_directory):
# Menerima List directory ke setiap file dalam src/uploads
# (karena hasil upload file pada web disimpan di src/uploads)
# Membalikan list berisi judul dari semua dokumen
    list_title = []
    for path in List_directory:
        document_html = open(path)
        soup = BeautifulSoup(document_html, 'lxml')
        title = soup.find('h1')
        list_title.append(title.text.strip())
    return list_title

def get_document_local(List_directory):
# Menerima list directory ke setiap file dalam src/uploads
# Mengambil isi berita dan mengembalikannya dalam bentuk list
# Hasil : ["dokumen1", "dokumen2"]
## Setelah itu menggunakan get_firstsentence untuk mendapatkan list kalimat pertamanya
    List_document = []
    for path in List_directory:
        document_html = open(path)
        soup = BeautifulSoup(document_html, 'lxml')
        teks_artikel = soup.find('body')
        string_teks = teks_artikel.get_text()
        List_document.append(string_teks)
    return List_document

def get_query(Query):
# Menerima Query dalam bahasa Indonesia dan mengembalikan sebagai list tuple kata dan jumlahnya
# Menghilangkan kata-kata yang tidak relevan dalam Query
# Contoh: "Pandemi Covid-19 sudah berjalan lebih dari delapan bulan, tetapi belum ada tanda-tanda penularan virus corona dapat dikendalikan"
# Hasil: [('pandemi', 1), ('covid19', 1), ('berjalan', 1), ('delapan', 1), ('tandatanda', 1), ('penularan', 1), ('virus', 1), ('corona', 1), ('dikendalikan', 1)]
    stop_words = set(stopwords.words('indonesian'))
    vector_query = Query.translate(str.maketrans('','',string.punctuation)).lower()
    tokenized_query = nltk.tokenize.word_tokenize(vector_query)
    filtered_words = []
    for word in tokenized_query:
        if word not in stop_words:
            filtered_words.append(word)
    filtered_words = nltk.FreqDist(filtered_words)
    filtered_words = filtered_words.most_common()
    return filtered_words

def get_listsemuadokumen():
# Mengembalikan file yang terdapat dalam folder src/uploads
# Untuk ditunjukkan pada website
# Hasil: ['namafile1.html', 'namafile2.html']
    path = os.path.dirname(os.path.abspath(__file__))
    path_to_uploads = os.path.join(path, 'uploads')

    list_namadokumen = os.listdir(path_to_uploads)
    return list_namadokumen


def get_linktoredirect(list_semuadokumen):
# Menerima list nama dokumen yang berada pada file uploads
# Mengembalikan list ditambahkan uploaded/ untuk redirect ketika memencet judul hasil query
# Hasil: ["uploaded/filename", ...]
    list_namadokumen = get_listsemuadokumen()
    list_toreturn = []
    for path in list_namadokumen:
        string = "uploaded/" + path
        list_toreturn.append(string)
    return list_toreturn

def scrape_local(InputQuery):
    path = os.path.dirname(os.path.abspath(__file__))
    path_to_uploads = os.path.join(path, 'uploads')

    # List isi path ke folder uploads
    list_dir = get_link_local(path_to_uploads)

    # List title setiap dokumen
    list_title_local = get_title_local(list_dir)

    # List isi berita tiap dokumen
    list_dokumen_local = get_document_local(list_dir)

    # Query yang sudah dijadikan vektor
    query = get_query(InputQuery)

    # List berisi kalimat pertama tiap dokumen
    list_fsentence_local = get_firstsentence(list_dokumen_local)

    # List berisi kalimat yang sudah diproses menjadi vektor tiap dokumen
    list_processedwords_local = get_vectorwords(list_dokumen_local)

    # List similarity tiap dokumen terhadap query
    list_similarity_local = get_similarity(query, list_processedwords_local)

    # List banyak kata tiap dokumen
    list_banyakkata_local = get_banyakkata(list_processedwords_local)

    # List untuk list_link_local
    list_alldocuments_local = get_listsemuadokumen()

    # List berisi link ke dokumen tersebut
    list_link_local = get_linktoredirect(list_alldocuments_local)

    # Dictionary yang akan digunakan
    scrape_result = [{
                        "link"      : val[0],
                        "title"     : val[1],
                        "content"   : val[2],
                        "words"     : val[3],
                        "fsentence" : val[4],
                        "similarity": val[5],
                        "count"     : val[6]}
                        for val in zip(list_link_local, list_title_local, list_dokumen_local, list_processedwords_local, list_fsentence_local, list_similarity_local, list_banyakkata_local)]
    return scrape_result

## Cek fungsi scrape_local
#namadokumen = get_listsemuadokumen()
#print_list(namadokumen)
#dictionary = scrape_local("bola adalah kesukaan saya")
#print(dictionary)



# Check isi dari scraping_results)
#print_similarity(scraping_results)
#print(search_results[0])
##Cara ngambil value dari list of dictionary:
#search_results[i].get("content")
#^^ngambil isi berita

# to scrape: 
# 1. text dari news article tag class_='read__content'
# 2. title dari news article h1 > class = 'read__title', coba h1 tag dulu baru read__title atau find class langsung
# 3. link tadi
# 4. 
# jadiin dictionary [link, judul, text, parsed_text, kalimat_pertama] //bisa ada update kalo butuh yang lain
# tambahin hasil similarity dengan query


## TENTUIN BERAPA DOKUMEN YANG MAU DIAMBIL
## PAKE FOR LOOP BUAT NEXT PAGE

## BERSIHIN GITHUB
## src berisi source code
## test berisi dokumen uji
## doc berisi laporan

## Delete file yang gaperlu di github