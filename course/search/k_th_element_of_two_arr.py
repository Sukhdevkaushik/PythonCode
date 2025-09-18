def k_th_element(a, b, k):
    a += b
    a.sort()
    print(a)
    return a[k -1]
    #low = 0
    #high = len(a) -1
    #while low <= high:
    #    mid = (high + low) // 2
    #    if a[mid] == k:
    #        return mid
    #    elif a[mid] > k:
    #        high = mid - 1
    #    else:
    #        low =  mid + 1
    #return 0

a = [2, 3, 6, 7, 9]
b = [1, 4, 8, 10]
k = 5
print(k_th_element(a, b, k))