def reverse_string(_reverse_string):
    if _reverse_string == "":
        return None
    lst = []
    reversed_string = ""
    for value in _reverse_string:
        lst.append(value)
    for _ in range(len(lst)):
        reversed_string = reversed_string + lst.pop()
    return reversed_string

def consecutive_num(blocks, k):
    curr_count = 0
    str_len = len(blocks)
    sum = str_len
    for i in range(str_len - k  + 1):
        curr_count = 0
        for j in range(i, i + k):
            if blocks[j] == "w":
                curr_count += 1
        sum = min(sum, curr_count)    
    return sum

def minimumRecolors(blocks: str, k: int) -> int:
    n = len(blocks)
    current_white_count = 0
    min_operations = n

    for i in range(n):
        if blocks[i] == 'W':
            current_white_count += 1
        if i >= k - 1:
            min_operations = min(min_operations, current_white_count)
    return min_operations

#blocks = "WBBWWBBWBW"
#k = 7
#print(minimumRecolors(blocks, k))  # Output should be 3
def longestOnes(nums, k):
    max_consecutive  = 0
    counter = 0
    num = 0
    for val in nums:
        if counter >= k:
            counter = 0
            max_consecutive = max(max_consecutive, num)
            num = 0
        if val == 1:
            num += 1
        if val == 0:
            num += 1
            counter += 1
    max_consecutive = max(max_consecutive, num)
    return max_consecutive

nums = [1,1,1,0,0,0,1,1,1,1,0]
print(longestOnes(nums, 2))

#consecutive_string = "wbbwwbbwbw"
#print(consecutive_num(consecutive_string, 7))

#_reverse_string = "sukhdev"
#print(reverse_string(_reverse_string))
    