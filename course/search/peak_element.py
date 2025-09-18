def peak_element(arr):
    high = len(arr)
    if high == 0:
        return False
    if high == 1:
        return True
    
    if arr[0] > arr[1]:
        return True
    if arr[-1] > arr[-2]:
        return True
    low = 0 
    high = high - 2
    
    while low <= high:
        mid = (low + high) // 2
 
        if arr[mid] > arr[mid -1] and arr[mid] > arr[mid + 1]:
            return True
        elif arr[mid] < arr[mid + 1]:
            low = mid + 1
        else:
            high = mid - 1
    return False



arr = [1, 2, 4, 5, 7, 8, 3]
print(peak_element(arr))