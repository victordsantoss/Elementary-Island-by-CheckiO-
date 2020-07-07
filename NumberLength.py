def number_length (a: int):
    resultado = 0
    if a == 0:
        return 1

    while a != 0:
        a //= 10
        resultado += 1

    return resultado
