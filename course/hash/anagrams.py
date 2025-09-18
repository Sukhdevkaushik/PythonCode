def anagrams(s1, s2):
    ''' '''
    result = {}
    for char in s1:
        result[char] = result.get(char, 0) + 1
    for char in s2:
        result[char] = result.get(char, 0) - 1
    
    for key, value in result.items():
        if value != 0:
            return False
    return True

s1 = 'geeks'
s2 = 'kseeg'
print(anagrams(s1, s2))