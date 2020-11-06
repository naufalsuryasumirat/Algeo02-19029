from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import nltk
import string
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
"""cars = [('word1', 10), ('word2', 20), ('word3', 12)]
cars2 = [('word2', 1), ('word3', 2), ('word4', 10)]

result = 0
for i in range (len(cars)):
    for j in range (len(cars2)):
        if (cars[i][0] == cars2[j][0]):
            result += (cars[i][1] * cars2[j][1])
print(result)"""

import math

query_v1 = [('apple', 1), ('banana', 1)]
document1_v1 = [('banana', 2), ('apple', 3), ('tomato', 1)]
document2_v1 = [('banana', 1), ('ginger', 1), ('tomato', 1), ('triangle', 1)]
document3_v1 = [('queen', 1), ('ginger', 1), ('vendor', 1), ('tomato', 2)]

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

def panjang_listvektor(List):
    panjang = 0
    for i in range (len(List)):
        panjang += List[i][1] * List[i][1]
    return math.sqrt(panjang)

def similarityList(LQuery, LDocument):
    dot_product = 0
    for i in range (len(LQuery)):
        for j in range(len(LDocument)):
            if (LQuery[i][0] == LDocument[j][0]):
                dot_product += (LQuery[i][1] * LDocument[j][1])
                break
    return (dot_product)/(panjang_listvektor(LQuery) * panjang_listvektor(LDocument))

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

factory = StemmerFactory()
stemmer = factory.create_stemmer()
sentence = 'Perekonomian di ke pada dari Indonesia sedang dalam pertumbuhan yang membanggakan dan sangat baik'
output   = stemmer.stem(sentence)
#print(output)

kalimat = "Andi kerap melakukan transaksi rutin secara daring atau online. Menurut Andi belanja online lebih praktis & murah."
kalimat = kalimat.translate(str.maketrans('','',string.punctuation)).lower()
stop_words = set(stopwords.words('indonesian'))
tokens = nltk.tokenize.word_tokenize(kalimat)

filtered = []

for i in tokens:
    if i not in stop_words:
        filtered.append(i)

kemunculan = nltk.FreqDist(filtered)
kemunculan2 = kemunculan.most_common()
print(kemunculan2)

sentence1 = [('word1', 7), ('word2', 5), ('word3', 4)]
sentence2 = [('word2', 11), ('word4', 3), ('word1', 1)]

hasil = 0
for i in range (len(sentence1)):
    for j in range (len(sentence2)):
        if (sentence1[i][0] == sentence2[j][0]):
            hasil += (sentence1[i][1] * sentence2[j][1])
            break
    


# to scrape: 
# 1. text dari news article tagclass_='read__content'
# 2. title dari news article h1 > class = 'read__title', coba h1 tag dulu baru read__title atau find class langsung