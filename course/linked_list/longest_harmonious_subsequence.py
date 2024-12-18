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
print(longest_harmonious_subsequence(nums))
