def sub_copy(text, n):
    size = 2
    if size > len(text):
        size = len(text)
    substr = text[:size]
    result = ""
    for i in range(n):
        result = result + substr
    return result
print(sub_copy("abcdef", 2))
print(sub_copy("p", 3))
