from typing import Iterable

def remove_all_before (items: list, border: int):
    i = 0
    
    if not items:
        return items

    # Verifica se o elemento está contido na lista
    if border in items:
        while i < len (items):
            if items[i] != border:
                items.pop (i)
            else:
                return items
    else:
        return items

    