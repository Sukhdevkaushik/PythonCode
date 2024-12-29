#====================================================
#brutw force approach
#====================================================
def max_prod_subarr(arr):
    n = len(arr)
    max_prod = float("-inf")
    for i in range(n):
        product = 1
        for j in range(i, n):
            product *= arr[j]
            max_prod = max(max_prod, product)
    return max_prod
arr = [-2, 6, -3, -10, 0, 2]
print(max_prod_subarr(arr))
#====================================================
#batter approach
#====================================================

def Maximum_Product_Subarray(arr):

    if len(arr) < 2 and arr != None:
        return abs(arr[0])

    max_num = arr[0]
    min_num = arr[0]
    result = 0

    for i in range(1, len(arr)):
        num = arr[i]
        if num < 0:
            max_num, min_num = min_num, max_num

        max_num = max(num, max_num * num)
        min_num = min(num, min_num * num)
        result = max(result, max_num)
    return result
#arr = [-2, 6, -3, -10, 0, 2]
#print(Maximum_Product_Subarray(arr))
