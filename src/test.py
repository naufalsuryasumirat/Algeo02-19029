# import Sastrawi package
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import math

#from urllib.request import urlopen as uRequest
#from bs4 import BeautifulSoup as BS

#pakai NLTK(Natural Language Toolkit) ada list stopwords
#from nltk.corpus import stopwords 
#from nltk.tokenize import word_tokenize 

# create stemmer
factory = StemmerFactory()
stemmer = factory.create_stemmer()

# stem
sentence = 'Perekonomian di ke pada dari Indonesia sedang dalam pertumbuhan yang membanggakan dan sangat baik'
output   = stemmer.stem(sentence)
# print(output)

# importing nltk
import nltk

import string
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords

kalimat = "Andi kerap melakukan transaksi rutin secara daring atau online. Menurut Andi belanja online lebih praktis & murah."
kalimat = kalimat.translate(str.maketrans('','',string.punctuation)).lower()

stop_words = set(stopwords.words('indonesian'))
tokens = nltk.tokenize.word_tokenize(kalimat)

filtered = []

#algoritma buat ngilangin stopwords
for i in tokens:
    if i not in stop_words:
        filtered.append(i)

kemunculan = nltk.FreqDist(filtered)
#print(kemunculan.most_common())

###print(kemunculan.most_common())

#print(stopwords.words('indonesian'))
#nltk.download()


query = ['apple', 'banana']
document1 = ['apple', 'apple', 'apple', 'banana', 'banana', 'tomato']
document2 = ['ginger', 'tomato', 'banana', 'triangle']
document3 = ['queen', 'ginger', 'vendor', 'tomato', 'tomato']

# query_v2 dengan menggunakan semua element dari semua dokumen
# urutannya adalah jumlah 'apple', 'banana', 'tomato', 'ginger', 'triangle', 'queen', 'vendor'
# jumlah total kata unik : 7

query_v1 = [('apple', 1), ('banana', 1)]
document1_v1 = [('apple', 3), ('banana', 2), ('tomato', 1)]
document2_v1 = [('ginger', 1), ('tomato', 1), ('banana', 1), ('triangle', 1)]
document3_v1 = [('queen', 1), ('ginger', 1), ('vendor', 1), ('tomato', 2)]

print(similarityList(query_v1, document1_v1))
print(similarityList(query_v1, document2_v1))
print(similarityList(query_v1, document3_v1))

query_v2 = [1, 1, 0, 0, 0, 0, 0]
document1_v2 = [3, 2, 1, 0, 0 ,0 ,0]
document2_v2 = [0, 1, 1, 1, 1, 0, 0]
document3_v2 = [0, 0, 2, 1, 0, 1, 1]

print(similarity(query_v2, document1_v2))
print(similarity(query_v2, document2_v2))
print(similarity(query_v2, document3_v2))

#vektor_test1 = [0, 0, 2]
#vektor_test2 = [2, 3, 5]

# Algoritma menentukan panjang vektor
def panjang_vektor(Vektor):
    panjang = 0
    for i in range (len(Vektor)):
        panjang += Vektor[i] * Vektor[i]
    return math.sqrt(panjang)

# Algoritma menentukan similarity dua vektor (Query dengan Document)
def similarity(Query, Document):
    dot_product = 0
    for i in range (len(Query)):
        dot_product += Query[i] * Document[i]
    return (dot_product)/(panjang_vektor(Query) * panjang_vektor(Document))

#print(similarity(vektor_test1, vektor_test2))


# Algoritma mengalikan dua list vektor
def panjang_listvektor(List):
    panjang = 0
    for i in range (len(List)):
        panjang += List[i][1] * List[i][1]
    return math.sqrt(panjang)

# Algoritma menentukan similarity dua list vektor (Query dengan Document) dengan algoritma pencarian dan pencocokan
def similarityList(LQuery, LDocument):
    dot_product = 0
    for i in range (len(LQuery)):
        for j in range(len(LDocument)):
            if (LQuery[i][0] == LDocument[j][0]):
                dot_product += (LQuery[i][1] * LDocument[j][1])
    return (dot_product)/(panjang_listvektor(LQuery) * panjang_listvektor(LDocument))

#sentence1 = 
"""sentence2 = 'Ekonomi Di Indonesia Adalah'
output2 = stemmer.stem(sentence2)
outputkata = output2.split()"""

#sentence3 = 'Ekonomi Ekonomi Ekonomi'
#output3 = stemmer.stem(sentence3)
#outputkata2 = output3.split()

#coba_input = input()

"""def toVektor(Sentence):
    array_sentence = (stemmer.stem(Sentence)).split()
    #array_out =
    #print(array_sentence)
    for i in array_sentence:

        for j in array_sentence:
            if (array_sentence[i] == array_sentence[j]) :
                del array_sentence[j]"""

### toVektor(coba_input)


# Web Scraping
# 1. kompas.com
# --> article__asset



#print(outputkata2)

#gunakan .split untuk tokenizing (memasukkan tiap kata dalam kalimat ke dalam array)

#print(output)
#print(output[7])

#print(output2)
#print(output2[0])
#print(outputkata[0])
#print(outputkata)

# ekonomi indonesia sedang dalam tumbuh yang bangga

#print(stemmer.stem('Mereka meniru-nirukannya'))

# mereka tiru

#print("Anjay Mabar")
#nama = input("Nama : ")
#print("Halo " + nama)

#tambahin ke readme cara buka .\Algeo\Scripts\activate untuk aktivasi virtualenv