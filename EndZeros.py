def end_zeros (num: int):
    aux = []
    i = 0

    if num == 0:
        return 1

    # É feita a inversão do número para contagem dos 0's. 
    while num > 0:
        aux.append (num % 10)
        num //= 10

    while aux[i] == 0:
        i += 1

    return i