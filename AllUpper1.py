def is_all_upper (text: str):
    i = 0
    resposta = True

    while i < len (text):
        if (text[i] >= 'A' and text[i] <= 'Z') or (text[i] == ' ') or (text[i] >= '1' and text[i] <= '9'):
            resposta = True
        else:
            resposta = False
        i += 1

    return resposta
