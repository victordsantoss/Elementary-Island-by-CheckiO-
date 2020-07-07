def beginning_zeros (number: str):
    i = 0
    contador = 0

    if not number:
        return 0
    else:
        while i < len (number):
            if number[i] == '0':
                contador += 1
            else:
                break
            i += 1
            
    return contador
