def checkio (number : int):
    result = 1

    while number > 0:
        if number % 10 != 0:
            result *= number % 10
            number //= 10
        else:
            number //= 10
            
    return result   