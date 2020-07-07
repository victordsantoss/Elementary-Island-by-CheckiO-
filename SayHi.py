def say_hi (name: str, age: int):
    aux = "Hi. My name is "
    aux2 = " and I'm "
    aux3 = " years old"
    idadeStr = str (age)
    
    final = aux + name + aux2 + idadeStr + aux3
    return final
