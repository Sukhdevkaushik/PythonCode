#def bubble_sort(arr):
#    """ """
#    for i in range(len(arr) -1, 0, -1):
#        for j in range(i):
#            if arr[j] > arr[j + 1]:
#                arr[j], arr[j + 1] = arr[j + 1], arr[j]
#    return arr
#arr = [1,3,4,7,8,2,5]
#print(bubble_sort(arr))

def bubble_sort(arr):
    if len(arr) <=0:        
        return None
    for i in range(len(arr) -1, 0, -1):
        for j in range(i):
            if arr[i] < arr[j]:
                arr[j], arr[i] = arr[i], arr[j]
    return arr

print(bubble_sort([4,2,6,5,1,3]))
