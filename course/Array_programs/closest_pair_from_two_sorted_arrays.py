def func(arr1, arr2, x):
    left = 0
    right = len(arr2) - 1
    diff = 922337203684575

    while (left < len(arr1) and right >= 0):

        if abs(arr1[left] + arr2[right] - x) < diff:
            left_result = left
            right_result = right
        diff = abs((arr1[left] + arr2[right]) - x)


        if arr1[left] + arr2[right] > x:
            right -= 1
        else:
            left += 1

    return (arr1[left_result], arr2[right_result])




arr1 = [1, 4, 5, 7]
arr2 = [10, 20, 30, 40]
x = 38
print(func(arr1, arr2, x))