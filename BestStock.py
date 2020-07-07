# Você recebe os preços atuais das ações e retorna a chave do elemento que custar mais

'''
def main ():
    dicionario = {}
    i = 0

    # Implementação EOF
    while True:
        try:
            valor = float (input ())
            dicionario[i] = valor
            i += 1
        except EOFError:
            break

    # Impressão das chaves e dos valores do dict
    for k,v in dicionario.items():
        print (k, " - ", v)

    print (best_stock(dicionario))
'''
def best_stock (a):
    maior = 0

    for k,v in a.items ():
        if v > maior:
            maior = v
            resposta = k

    return resposta

# main ()