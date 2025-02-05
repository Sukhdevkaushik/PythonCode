def insertion_sort(arr):
    """ """
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1
        while temp < arr[j] and j > -1:
            arr[j + 1] = arr[j]
            arr[j] = temp            
            j -= 1
    return arr

arr = [3, 1, 2, 4, 5, 8, 7]
print(insertion_sort(arr))