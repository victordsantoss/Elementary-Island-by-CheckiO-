def between_markers (text: str, begin: str, end: str):

    i = 0
    result = []

    while i < len (text):
        if text[i] == begin:
            j = i+1
            while text[j] != end:   
                result.append (text[j])
                j += 1
            break
        i += 1
    return ''.join (result)
