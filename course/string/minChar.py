def minChar(s):
    """ """
    if len(s) < 1:
        return 0
    #Cal the LPS array
    rev_s = s[::-1]
    combined = s + "#" + rev_s
    count = 0
    i = 1
    n = len(combined)
    lps = [0] * n
    while i < n:
        if combined[i] == combined[count]:
            count += 1
            lps[i] = count
            i += 1
        else:
            if count != 0:
                count = lps[count -1]
            else:
                lps[i] = 0
                i+= 1
    return len(s) - lps[-1]
s = "abc"
print(minChar(s))