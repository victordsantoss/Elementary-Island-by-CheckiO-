def max_digit (number: int):
    maior = 0

    while number > 0:
        aux = number % 10
        if aux > maior:
            maior = aux
        number //= 10

    return maior    