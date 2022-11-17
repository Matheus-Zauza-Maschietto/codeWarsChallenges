def order(sentence):
    listWords = sentence.split()
    enum_setence = []
    cont = 0
    for index in range(len(listWords)+1):
        for word in listWords:
            if str(index) in word:
                enum_setence.insert(index, word)
                listWords.remove(word)
                break
    return " ".join(enum_setence)

print(order("publi1c 4her but2 s3ame"))
