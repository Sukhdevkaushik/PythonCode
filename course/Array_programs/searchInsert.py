def searchInsert(nums, target) -> int:
    for i in range(len(nums)):
        print(nums[i])
        if nums[i] >= target:
            print("i ke value")
            return i
    return len(nums) + 1
     
nums = [1,3,5,6]
target = 5
print(searchInsert(nums, target))
