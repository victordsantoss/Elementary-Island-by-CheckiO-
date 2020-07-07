def checkio (array):
    i = 0
    soma = 0
    
    # Verifica se há elementos na matriz
    if not array:
        return 0
    else:
        while i < len (array):
            if (i % 2 == 0):
                soma += array[i]
                i += 1
            else:
                i += 1
        resultado = soma * array[i-1] 
        return resultado
    