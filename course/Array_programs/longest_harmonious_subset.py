def longest_harmonious_subset(nums):
    """ """
    nums.sort()
    right = 1 
    left = 0
    max_num = 0
    while right < len(nums):
        diff = nums[right] - nums[left] 
        if diff == 1:
            max_num = max(max_num, right - left + 1)
        if diff <= 1:
            right += 1
        else:
            left += 1
    return max_num



nums = [1,2,3,4]
print(longest_harmonious_subset(nums))