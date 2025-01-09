#Strings Rotations of Each Other
def areRotations(s1, s2):
    #create the LPS table
    n = len(s2)
    i = 1
    count = 0
    lps = [0] * n
    while i < n:
        if s2[i] == s2[count]:
            count += 1
            lps[i] =  count
            i += 1
        else:
            if count != 0:
                count = lps[count -1]
            else:
                lps[i] = 0
                i += 1
    #compare the code with the help of lps
    s1 = s1 + s1
    s1_len = len(s1)
    j =0
    i = 0
    while i < s1_len:
        if s2[j] == s1[i]:
            j += 1
            i += 1
            if j == n:                
                return True
        else:
            if j!= 0:
                j = lps[j-1]
            else:
                i += 1
    return False

s1 = "abcd"
s2 = "cdab"
print(areRotations(s1, s2))
