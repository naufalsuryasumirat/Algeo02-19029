import requests
import nltk
import string
import math
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords

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

# test query
query = [('gol', 1), ('penalti', 1), ('kiper', 2), ('gawang', 2)]

list_url = get_link("https://bola.kompas.com/liga-inggris")
add_link(list_url, "?page=all#page2")

## print isi list_url dengan rapi
print_list(list_url)

## print isi array list_url
print(len(list_url))

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
print_list(list_similarity)

# to scrape: 
# 1. text dari news article tag class_='read__content'
# 2. title dari news article h1 > class = 'read__title', coba h1 tag dulu baru read__title atau find class langsung
# 3. link tadi
# 4. 
# jadiin dictionary [link, judul, text, parsed_text, kalimat_pertama] //bisa ada update kalo butuh yang lain
# tambahin hasil similarity dengan query