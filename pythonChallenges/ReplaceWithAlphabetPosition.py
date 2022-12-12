def alphabet_position(text):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    if text == ' ':
        return ''
    else:
        alfanumerado = text
        for c in range(10):
            alfanumerado = alfanumerado.replace(str(c), " ")
        alfanumerado = ' '.join([item.replace(item, str(alfabeto.find(item.lower())+1)) for item in alfanumerado.strip()])
        return alfanumerado
    
print("@@@"+alphabet_position('0 0 0 0')+"@@@")
