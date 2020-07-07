def correct_sentence (text: str):
    aux = text[1:]
    text = text[0].upper ()
    text += aux
    
    if text[len (text)-1] != '.':
        text = text + '.'
    return ''.join (text)
