def Anagram(s1, s2):
    """ """
    if len(s1) != len(s2):
        return False
    s1_dict = {}
    

    for value in s1:
        s1_dict[value] = s1_dict.get(value, 0) + 1        
    for value in s2:
        s1_dict[value] = s1_dict.get(value, 0) - 1

    for _, value in s1_dict.items():
        if value != 0:
            return False
    return True

s1 = "a"
s2 = "b"
print(Anagram(s1, s2))
