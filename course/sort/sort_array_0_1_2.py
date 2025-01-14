#DNF algo
def sort012(arr):
    n = len(arr) -1
    if n < 1:
        return arr
    start = 0
    end = n
    mid = 0
    while mid <= end:
        if arr[mid] ==0:
            arr[start], arr[mid] = arr[mid], arr[start]
            start += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[end] = arr[end], arr[mid]
            end -= 1
    return arr

arr = [0, 1, 2, 0, 1, 2]
print(sort012(arr))
