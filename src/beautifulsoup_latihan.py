import requests
from bs4 import BeautifulSoup

#result = requests.get("https://www.kompas.com")
result = requests.get("https://bola.kompas.com/liga-inggris")
## link yang dapat digunakan: https://bola.kompas.com/liga-inggris
## yang dicari class="article__link"

print(result.status_code)
## 200 means accessable

#print(result.headers)

source = result.content
#print(source)

soup = BeautifulSoup(source, 'lxml')

#links = soup.find_all("a") #<a class="article__link"
#print(links)
#print("\n")

## print semua link dengan tersusun tiap link tiap line terminal
#for link in range (len(links)):
    #print(links[link])

"""for link in links:
    ## jika ingin mencari About
    if "article__link" in link.text:
        print(link)
        print(link.attrs['href'])
        ## attribute / attrs href (print content dalam href)"""

## HEY tadi pip3 install --upgrade lxml sama pip3 install cssselect
## PUSH ke github

## menggunakan tag
list_url = []

## meng-ekstrak h3 pada link (semua link yang terdapat pada main page liga inggris kompas)
## dan memasukkan tiap link ke dalam array list_url

def get_link(request):
    # request = "https://bola.kompas.com/liga-inggris"
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

for h3_tag in soup.find_all("h3"):
    a_tag = h3_tag.find('a')
    list_url.append(a_tag.attrs['href'])
#print(list_url) ##print berantakan

def print_list(List):
    for i in range(len(List)):
        print(List[i])

def add_link(List, string):
    # untuk menambahkan "?page=all#page2" pada link agar memperlihatkan seluruh isi artikel berita (karena biasanya terbagi 2 halaman lebih)
    for i in range(len(List)):
        List[i] += string

## print isi list_url dengan rapi
print_list(list_url)

## print isi array list_url
print(len(list_url))

add_link(list_url, "?page=all#page2")
print_list(list_url)

string_dokumen = []

for link in range(len(list_url)):
    links = requests.get(list_url[link])
    src = links.content
    bsoup = BeautifulSoup(src, 'lxml')
    article_text = bsoup.find_all('div', class_='read__content')
    string_teks = article_text[0].get_text()
    string_dokumen.append(string_teks)
### buat jadi function

def get_document(List_link):
    List_document = []
    for link in range(len(List_link)):
        links = requests.get(List_link[link])
        src = links.content
        bsoup = BeautifulSoup(src, 'lxml')
        article_text = bsoup.find_all('div', class_ = 'read__content')
        string_teks = article_text[0].get_text()
        List_document.append(string_teks)
    return List_document

print_list(string_dokumen)

list_title = []

for link in range(len(list_url)):
    links = requests.get(list_url[link])
    src = links.content
    bsoup = BeautifulSoup(src, 'lxml')
    article_title = bsoup.find('h1', class_='read__title')
    list_title.append(article_title.text.strip())

def get_title(List_link):
    List_title = []
    for link in range(len(List_link)):
        links = requests.get(List_link[link])
        src = links.content
        bsoup = BeautifulSoup(src, 'lxml')
        article_title = bsoup.find('h1', class_ = 'read__title')
        List_title.append(article_title.text.strip())
    return List_title

print_list(list_title)



"""for link in range(len(list_url)):
    links = requests.get(list_url[link])
    #print(links.status_code) ## cek web bisa diakses atau engga
    src = links.content
    bsoup = BeautifulSoup(src, 'lxml')
    article_text = bsoup.find_all('div', class_='read__content')
    for text in range(len(article_text)):
        string_text = ""
        #print(article_text[text].get_text()) ## print content news article
        if (text != 1) :
            string_text += " "
        string_text += article_text[text].get_text()
        if (text == 3) :
            break
    #print(string_text)
    print(article_text[0].get_text())
    #print(article_text.get_text()) ##salah
    break"""

"""for plus_link in range(len(list_url)):
    list_url[plus_link] += "?page=all#page2"
    # untuk show all pada tiap dokumen"""

"""for print_list in range(len(list_url)):
    print(list_url[print_list])"""

"""for link in range(len(list_url)):
    links = requests.get(list_url[link])
    src = links.content"""



# habis buka tiap link dari liga inggris bola buka cari 

# to scrape: 
# 1. text dari news article tagclass_='read__content'
# 2. title dari news article h1 > class = 'read__title', coba h1 tag dulu baru read__title atau find class langsung
# 3. link tadi
# 4. 
# jadiin dictionary [link, judul, text, parsed_text, kalimat pertama] (tentative)
# tambahin hasil similarity dengan query