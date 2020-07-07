def split_pairs (a):
    i = 0
    cont = 1
    lista = []

    if not a:
        return lista
    else:
        if len (a) % 2 == 0:
            while cont < len (a):
                lista.append (a[i]+a[cont])
                i += 2
                cont += 2
        else:
            while True:
                if i == len (a)-1:
                    lista.append (a[i] + '_')
                    break
                else:
                    lista.append (a[i]+a[cont])
                    i += 2
                    cont += 2             
    return lista 