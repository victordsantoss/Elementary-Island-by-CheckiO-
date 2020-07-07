from typing import Iterable

def replace_first (items: list):
    
    i = 0
    cont = 1

    if not items:
        return items
    else:
        tmp = items[0]
        while i < len (items)-1:
            aux = items [cont]
            items [i] = aux
            i += 1
            cont += 1
        items [len (items)-1] = tmp

    return items
