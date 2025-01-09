#KMP Algorithm for Pattern Searching
def pattern_searching(txt, pat):
    result = []
    n, m = len(txt), len(pat)
    
    for i in range(n - m + 1):  # Loop through the text, up to the point where the pattern can fit
        match = True
        for j in range(m):  # Loop through the pattern
            if txt[i + j] != pat[j]:  # Compare characters of pattern and text
                match = False
                break  # Break if mismatch occurs
        if match:  # If the entire pattern matches, record the starting index
            result.append(i)
    
    return result

#txt = "abcab"
#pat = "ab"
#print(pattern_searching(txt, pat))
def get_lps(pat):
    """To genrate lps arr"""
    lps = [0] * len(pat)
    count = 0
    i = 1
    while i < len(pat):        
        if pat[i] == pat[count]:
            count += 1
            lps[i] = count
            i += 1
        else:
            if count != 0:
                count = lps[count- 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def pattern_searching_bast(txt, pat):
    lps = get_lps(pat)
    n = len(txt)
    m = len(pat)
    result = []

    i = 0
    j = 0
    while i < n:
        if txt[i] == pat[j]:
            i += 1
            j += 1
        
            if j == m:
                result.append(i-j)
                j = lps[j -1]
        else:
            if j!= 0:
                j = lps[j - 1]
            else:
                i += 1
    return result


txt = "aabaacaadaabaaba"
pat = "aaba"
print(pattern_searching_bast(txt, pat))

