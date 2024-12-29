def max_arr_sum(arr, k):
    curr_sum = arr[0]
    max_sum = arr[0]

    for i in range(1, len(arr)):
        if curr_sum < 0:
            curr_sum = 0
        curr_sum += arr[i] 
        max_sum = max(max_sum, curr_sum)    
    return max_sum

arr = [1, -2, 3, -2 ]
print(max_arr_sum(arr, 3))