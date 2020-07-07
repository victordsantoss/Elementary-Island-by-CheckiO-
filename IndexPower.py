def index_power (matriz : list, n : int):
    i = 0

    while i < len (matriz):
        if i == n:
            resultado = matriz[n] ** n
            return resultado
        i += 1
    return -1