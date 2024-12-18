def reverse():
    lst = [1, 2, 3, 4, 5]
    print("before reverse")
    print(lst)
    first = 0
    last = len(lst) - 1
    while last > first:
        lst[first], lst[last] = lst[last], lst[first]
        last -= 1
        first += 1
    print("after reverse")    
    print(lst)
#print(reverse())

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
