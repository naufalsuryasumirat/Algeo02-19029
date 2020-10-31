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
print(output)

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
print(kemunculan.most_common())
#print(stopwords.words('indonesian'))
#nltk.download()
"""
vektor_test1 = [0, 0, 2]
vektor_test2 = [2, 3, 5]

def panjang_vektor(Vektor):
    panjang = 0
    for i in range (len(Vektor)):
        panjang += Vektor[i] * Vektor[i]
    return math.sqrt(panjang)

def similarity(Query, Document):
    dot_product = 0
    for i in range (len(Query)):
        dot_product += Query[i] * Document[i]
    return (dot_product)/(panjang_vektor(Query) * panjang_vektor(Document))

print(similarity(vektor_test1, vektor_test2))
"""
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
    array_out =
    print(array_sentence)
    for i in array_sentence:

        for j in array_sentence:
            if (array_sentence[i] == array_sentence[j]) :
                del array_sentence[j]

toVektor(coba_input)"""

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