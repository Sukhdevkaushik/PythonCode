def first_non_repeated(string):
    ''''''
    result = []
    for char in string:
        if char in result:
            result.remove(char)
        else:
            result.append(char)
    return result[0]

print(first_non_repeated("aabccde"))