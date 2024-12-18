
#def contain_duplicate(nums, k):
#    """ """
#    arr_len  = len(nums)
#    for i in range(arr_len):
#        number = nums[i]
#        if arr_len - 1 > i + k :
#            return False        
#        if number == nums[i + k]:
#            return True
#        i = i + 1
def contain_duplicate(nums, k):
    """ """
    data_map = {}
    for i in range(len(nums)):
        if nums[i] in data_map and abs(i - data_map[nums[i]]) <= k:
            return True        
        data_map[nums[i]] = i 
    return False
    
        
num = [1,2,3,1]
k = 3
print(contain_duplicate(num, k))