def Smallest_Positive_Missing(arr):
    #Cycle sort        
    n = len(arr)
    for i in range(n):
        while 1<=arr[i] <= n and arr[i]!=arr[arr[i]-1]:
            temp = arr[i]
            arr[i] = arr[ arr[i]-1 ]
            arr[temp-1] = temp
                
    #checking missing element
                
    for i in range(1, n+1):
        if i != arr[i-1]:
            return i
                
    return n+1

arr = [2, -3, 4, 1, 1, 7]
print(Smallest_Positive_Missing(arr))