def toVektor(Sentence):
    array_sentence = (stemmer.stem(Sentence)).split()
    #array_out =
    #print(array_sentence)
    for i in array_sentence:

        for j in array_sentence:
            if (array_sentence[i] == array_sentence[j]) :
                del array_sentence[j]