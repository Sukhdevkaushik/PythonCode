def for_sum(nums, target):
    result = []
    sum = 0
    nums.sort()
    print(nums)
    for i in range(len(nums) - 3):
        for j in range(i + 1, len(nums) - 2):
            print("i ke value %s", nums[i])
            print("j ke value %s", nums[j])
            left = j
            right = len(nums) - 1
            while left < right:
                sum = nums[i] + nums[j] + nums[left] + nums[right]
                print("sum ke value %s", sum)
                if sum == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                if sum > target:
                    right -= 1
                else:
                    left -= 1

    return result

nums = [1, 0, -1, 0, -2, 2]
target = 0
print(for_sum(nums, target))