def alphabet_position(text):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    for c in range(10):
        text = text.replace(str(c), " ")
    alfanumerado = ' '.join([item.replace(item, str(alfabeto.find(item.lower())+1)) for item in text.strip()])
    return alfanumerado
    
print("@@@"+alphabet_position('0 0 0 0')+"@@@")
