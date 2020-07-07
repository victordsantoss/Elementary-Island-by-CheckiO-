def find_message (texto : str):
    mensagem = []
    i = 0

    while i < len (texto):
        if texto[i] >= 'A' and texto[i] <= 'Z':
            mensagem.append (texto[i])
            i += 1
        else:
            i += 1

    return ''.join(mensagem)
