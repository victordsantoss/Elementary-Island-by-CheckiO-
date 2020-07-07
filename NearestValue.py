def nearest_value (values: set, one: int):

    recebeSet = list (values)
    recebeSet.sort ()
    contador = 0

    if one < recebeSet[0]:
        return recebeSet[0]   
    else: 
        while contador < len (recebeSet):
            if recebeSet[contador] == one:
                return recebeSet[contador]
            elif recebeSet[contador] < one and recebeSet[contador+1] > one:
                break
            elif recebeSet[len (recebeSet)-1] < one:
                return recebeSet[len (recebeSet)-1]
            contador += 1

    # Pega o valor absoluto das diferenças da esquerda e direita
    esquerda = one - recebeSet[contador]
    direita = abs (one - recebeSet[contador+1])

    if esquerda <= direita:
        return recebeSet[contador]
    else:
        return recebeSet[contador+1]
