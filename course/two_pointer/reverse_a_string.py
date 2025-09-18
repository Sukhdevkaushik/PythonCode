def reverse_string(s):

    '''count = len(s)
    while count ==0:
        return s
    return reverse_string(s[1:]) + s[0]'''

    reversed_str = ""
    for char in s:        
        reversed_str = char + reversed_str
    return reversed_str

    '''n = reversed(s)
    return "".join(n)'''

    
    #left = 0
    #right = len(s) -1

    #while left < right:
    #    s[left], s[right] = s[right], s[left]
    #return s


s = ['sukhdev','kau shik']
print(reverse_string(s))