#Count Inversions
#brute force 
def count_inversions(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(i +1, len(arr)):
            if arr[i] > arr[j]:
                count += 1
    return count
arr = [10, 10, 10]
print(count_inversions(arr))


    