def first_word (text: str):
    i = 0
    primeira = []

    while i != len (text):
        if text[i] != ' ':
            primeira.append (text[i])
            i += 1
        else:
            break

    return ''.join (primeira)
