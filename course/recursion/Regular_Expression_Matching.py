def Regular_Expression_Matching(s, p):

    pattrens = list(p)
    
    for pattren in pattrens:
        for string in s:
            if pattren != string:
                return False
            if pattren == "*":
                


s = "aa"
p = "a*"
print(Regular_Expression_Matching(s, p))