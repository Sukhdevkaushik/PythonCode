def merge_without_extra_space(a , b):
    n = len(a)
    m = len(b)
    mid = (n + m + 1) // 2
    
    while mid > 0:
        i = 0
        j = mid
        print("xxxxxxxxxxxxx")
        while j < n + m:

            if j < n and a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
            
            if j >= n and i < n and a[i] >  b[j - n]:
                a[i], b[j - n] = b[j - n], a[i]
            
            if i >= n and b[i - n] > b[j - n]:
               b[i - n], b[j - n] = b[j - n], b[i - n]

            i += 1
            j += 1
        if mid == 1:
            break            
        mid = mid // 2
    return (a, b)

a = [2, 4, 7, 10]
b = [2, 3]

print(merge_without_extra_space(a , b))
