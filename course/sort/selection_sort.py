def selection_sort(arr):
    """ """
    min_index = 0
    for i in range(len(arr) -1):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        if i != min_index:
            arr[i], arr[min_index] \
                = arr[min_index], arr[i]                
    return arr
arr = [1, 5, 4, 3, 2]
print(selection_sort(arr))