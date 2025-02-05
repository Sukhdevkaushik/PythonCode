def hIndex(citations):
    n = len(citations)
    if n < 1:
        return None
    result_arr = [0] * (n + 1)
    for value in citations:
        if value >= n:
            result_arr[n] += 1
        else:
            result_arr[value] += 1
    #Search based on count
    print(result_arr)
    idx = n
    s = result_arr[n]
    while s < idx:                
        idx -= 1
        s += result_arr[idx]
    return idx

citations = [3, 0, 5, 3, 0]
print(hIndex(citations))




