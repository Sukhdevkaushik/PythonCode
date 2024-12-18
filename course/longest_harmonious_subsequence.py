#def longest_harmonious_subsequence(nums):
#    lst = []
#    for i in range(len(nums)):
        
#        if i >= len(nums):
#            return len(lst)
        
#        if nums[i] in lst:
#            lst.append(nums[i])
#            print(lst)
        
#        if (nums[i] - nums[i + 1]) == 1:
#            lst.append(nums[i])
#            lst.append(nums[i + 1])
#        i = i + 1

def longest_harmonious_subsequence(nums):
    """ """
    lst = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if (nums[i] - nums[j] == 1):                
                lst.append(nums[j])                
            print(lst)
            j = j + 1
        print("done")
        i = i + 1
    print(lst)
    
nums = [1,3,2,2,5,2,3,7]
#print(longest_harmonious_subsequence(nums))


def merge_the_tools(string, k):
    num = 1
    data = ""
    for char in string:
        if num == k + 1:
            print(data)
            num = 1
            data = ""
        if num <=k and char not in data:
            data = data + char
        num += 1
    print(data)

#merge_the_tools('AABCAAADA', 3)

def rotateLeft(d, arr):
    temp = []
    for i in range(d, len(arr)):
        temp.append(arr[i])
    for i in range(d):
        temp.append(arr[i])
    return temp

#print(rotateLeft(4, [1,2,3,4,5,6]))

def arrayManipulation(n, queries):
    sum  = 0
    maxsum = 0
    arr = [0 for i in range(n + 2)]
    for i in range(len(queries)):
        start = queries[i][0]
        end = queries[i][1]
        num = queries[i][2]        
        arr[start] += num
        #if end + 1 < n:
        arr[end + 1] -= num        
    print(arr)
    for val in arr:
        sum = sum + val
        maxsum = max(sum, maxsum)
    return maxsum


n = 4
queries = [[2, 3, 603], [1, 1, 286], [4, 4, 882]]
print(arrayManipulation(n, queries))
