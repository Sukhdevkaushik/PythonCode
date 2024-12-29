def getMinDiff(arr,k):
    arr.sort()
    _min = 0
    _max = 0
    result = 0
    n = len(arr) - 1
    result = arr[n] - arr[0]
    if n < 1:
        return 0

    for i in range(1, n):
        #condition of checking element value less
        #then k
        if arr[i] < k:
            continue

        _max = max(arr[i -1] + k, arr[n] - k)
        _min = min(arr[i] - k, arr[0] + k)
        #_min = min(0, _min)
        # Avoid negative _min values
        if _min < 0:
            _min = 0

        result = min(result, _max - _min)
    return result
    
arr = [267, 466]
k = 611
print(getMinDiff(arr, k))
def _getMinDiff(arr, k):
    if len(arr) <= 1:
        return 0

    arr.sort()
    n = len(arr)
    result = arr[-1] - arr[0]

    for i in range(1, n):
        if arr[i] < k:
            continue

        # Compute max and min values after modification
        _max = max(arr[i - 1] + k, arr[-1] - k)
        _min = min(arr[i] - k, arr[0] + k)

        # Avoid negative _min values
        if _min < 0:
            _min = 0

        # Update the result
        result = min(result, _max - _min)

    return result


# Example Input
#arr = [380, 156, 781]
#k = 351
#print(_getMinDiff(arr, k))



