#Non Repeating Character

def non_rep_char(s):
    #to check if string only with 1 char
    if len(s) <2:
          return s
    
    #Update the count of each char in a dict
    occ_dict = {}
    for value in s:
        occ_dict[value] = occ_dict.get(value, 0) + 1
    
    #check the dict if char count 1 then return that
    for key, value in occ_dict.items():
        if value == 1:
            return key
    return -1

s = "qs"
print(non_rep_char(s))