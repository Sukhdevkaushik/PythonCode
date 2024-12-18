def maximum_average_subarray(nums, k):
    num = 0
    max_num = 0
    for i in range(len(nums) - k + 1):
        num = 0
        for j in range(i, k + i):    
            num += nums[j]            
        max_num = max(max_num, num)      
    return max_num / k

nums = [1,12,-5,-6,50,3]
k = 4
#print(maximum_average_subarray(nums, k))

def test(nums, k):
    current_sum = sum(nums[:k])
    max_sum = current_sum
    for i in range(k, len(nums)):
        current_sum = nums[i] - nums[i - k]
        max_sum = max(max_sum, current_sum)
    return max_sum / k

nums = [1,12,-5,-6,50,3]
k = 4
print(test(nums, k))
