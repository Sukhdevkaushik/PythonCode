def three_sum(nums, target):
    right = len(nums) - 1
    current_sum = 0
    closest_sum = 0
    nums.sort()
    for i in range(len(nums)):
        left = i + 1
        while left < right:
            sum =  nums[i] + nums[left] + nums[right]

            if current_sum == target:
                return current_sum

            if abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum

            if sum > target:
                right -= 1
            else:
                left += 1
    return sum

nums = [0,1,2]
target = 0
print(three_sum(nums, target))