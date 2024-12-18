def three_sum(nums):
    data = set()
    right = len(nums) - 1
    nums.sort()
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue  # Skip duplicates for the main number

        left = i + 1
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum > 0:
                right -= 1
            elif sum < 0:
                left += 1
            else:
                data.add((nums[i], nums[left], nums[right]))
                left += 1
    return list(data)

nums = [-1,0,1,2,-1,-4,-2,-3,3,0,4]
print(three_sum(nums))