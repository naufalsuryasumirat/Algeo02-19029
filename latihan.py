
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
document1_v1 = [('apple', 3), ('banana', 2), ('tomato', 1)]
document2_v1 = [('ginger', 1), ('tomato', 1), ('banana', 1), ('triangle', 1)]
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