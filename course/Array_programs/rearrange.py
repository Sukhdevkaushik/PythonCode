def rearange(arr):
    pointer1 = 0
    pointer2 = len(arr)
    while pointer1 < pointer2:
        if arr[pointer1] > arr[pointer2]:
           arr[pointer2] = arr[pointer1]
           pointer2 += 1
        else:
            pointer1 += 1
    return arr
arr = [40, 39, 36, 31, 37, 35, 34, 33, 32, 38]
print(rearange(arr))