def item_in_common(list1, list2):
    data = {}
    j = 0
    i = 0
    for i in list1:
        data[i] = True
    for index, j in enumerate(list2):
        if list2[index] in data:
            return True
    return False
        


list1 = [1,3,5,6]
list2 = [2,4,7]

def group_anagrams(strings):
    data = {}
    for string in strings:
        val = ''.join(sorted(string))
        if val in data:
            data[val].append(string)
        else:
            data[val] = [string]
    return list(data.values())
        


#print("1st set:")
#print( group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) )

#print("\n2nd set:")
#print( group_anagrams(["abc", "cba", "bac", "foo", "bar"]) )

#print("\n3rd set:")
#print( group_anagrams(["listen", "silent", "triangle", "integral", "garden", "ranged"]) )



"""
    EXPECTED OUTPUT:
    ----------------
    1st set:
    [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

    2nd set:
    [['abc', 'cba', 'bac'], ['foo'], ['bar']]

    3rd set:
    [['listen', 'silent'], ['triangle', 'integral'], ['garden', 'ranged']]

"""

#print(item_in_common(list1, list2))

def first_non_repeating_char(string):
    data = {}
    for val in string:
        print(val)
        data[val] = data.get(val, 0) + 1
    for val in string:
        print("sssssss %s", val)
        if data[val] == 1:
            return val
    return None


#print( first_non_repeating_char('leetclde') )

#print( first_non_repeating_char('hellh') )

def two_sum(nums, target):
    num_map = {}
    for index, val in enumerate(nums):
        required = target - val
        if required in num_map:            
            print(num_map)
            return [num_map[required], index]
        num_map[val] = index
    return []
#print(two_sum([5, 1, 7, 2, 9, 3], 10))  
#print(two_sum([4, 2, 11, 7, 6, 3], 9))  
#print(two_sum([10, 15, 5, 2, 8, 1, 7], 12))  
#print(two_sum([1, 3, 5, 7, 9], 10))  
#print ( two_sum([1, 2, 3, 4, 5], 10) )
#print ( two_sum([1, 2, 3, 4, 5], 7) )
#print ( two_sum([1, 2, 3, 4, 5], 3) )
#print ( two_sum([], 0) )

def _subarray_sum(nums, target):        
    for i in range(len(nums)):
        sum = nums[i]
        return_indx = [i]
        for j  in range(i + 1, len(nums)):
            sum = sum + nums[j]            
            if sum == target:
                return_indx.append(j)
                return return_indx
    return None

def subarray_sum(nums, target):
    sum_index = {0: -1}
    current_sum = 0
    for i, num in enumerate(nums):
        current_sum += num
        print("current sum %s", current_sum, "target %s", target, "sum index %s", sum_index)
        if current_sum - target in sum_index:
            return [sum_index[current_sum - target] + 1, i]
        sum_index[current_sum] = i
    return []


nums = [1, 2, 3, 4, 5]
target = 9
#print (subarray_sum(nums, target))

def remove_duplicates(my_list):
    unique_set = set()
    for val in my_list:
        unique_set.add(val)
    return unique_set

my_list = [1, 2, 3, 4, 1, 2, 5, 6, 7, 3, 4, 8, 9, 5]
#new_list = remove_duplicates(my_list)
#print(new_list)

def has_unique_chars(string):
    lst = []
    for val in string:
        if val in lst:
            return False
        lst.append(val)
    return True

#print(has_unique_chars('abcdefg')) # should return True
def _find_pairs(arr1, arr2, target):
    lst = []
    for i in range(len(arr1)):
        sum = arr1[i]
        for j in range(len(arr2)):
            sum  = sum + arr2[j]
            if sum == target:
                num = (arr1[i], arr2[j])
                lst.append(num)
            else:
                sum  = sum - arr2[j]
    return lst

def find_pairs(arr1, arr2, target):
    result = []
    set1 = set(arr1)
    for val in arr2:
        compnt = target - val
        if compnt in set1:
            num = (val, compnt)
            result.append(num)
    return result

arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 6, 8, 10]
target = 7
#pairs = find_pairs(arr1, arr2, target)
#print (pairs)

def longest_consecutive_sequence(nums):
    nums_set = set(nums)
    longest_consecutive_sequence = 0
    for num in nums:
        if num - 1 in nums_set:
            cur_sum = num
            current_sequence = 1            
            while cur_sum + 1 in nums_set:
                cur_sum += 1
                current_sequence += 1                
            longest_consecutive_sequence = max(longest_consecutive_sequence, current_sequence)    
    return longest_consecutive_sequence

def _longest_consecutive_sequence(nums):
    num_set = set(nums)
    longest_sequence = 0    
    for num in nums:
        if num - 1 not in num_set:
            current_num = num
            current_sequence = 1            
            while current_num + 1 in num_set:
                current_num += 1
                current_sequence += 1            
            longest_sequence = max(longest_sequence, current_sequence)
    return longest_sequence


#print(_longest_consecutive_sequence([100, 4, 200, 1, 3, 2]))

def validate_emp_id(emp_ids):
    data = []
    uppercase = 0
    digits = 0
    for emp_id in emp_ids:
        for char in emp_id:
            if char.isdigit():
                digits += 1
            if char.isupper():
                uppercase += 1
               
            if char in data:
                return "Invalid"
            data.append(char)
        if digits < 3 or uppercase < 2:
            return "Invalid"
        else:
            return "Valid"
        
emp_ids = ["B1CD102354", "B1CDEF2354"] 
#print(validate_emp_id(emp_ids))

def time_delta(t1, t2):
    from datetime import datetime
    date_format = "%a %d %b %Y %H:%M:%S %z"

    start_date = datetime.strptime(t1, date_format)
    end_date = datetime.strptime(t2, date_format)
    diff = start_date - end_date
    result = int(abs(diff.total_seconds()))
    print(result)

t1 = "Sat 24 Mar 2170 03:47:07 +0430"
t2 = "Mon 30 Dec 2272 20:27:41 -1000"
#time_delta(t1, t2)

def matchingStrings(stringList, queries):
    _count = 0
    data = []
    for query in queries:
        if query in stringList:
            _count = stringList.count(query)
            data.append(_count)
        else:
            data.append(0)
    return data

stringList = ['abcde', 'sdaklfj', 'asdjf', 'na', 'basdn', 'sdaklfj', 'asdjf', 'na', 'asdjf', 'na', 'basdn', 'sdaklfj', 'asdjf']
queries = ['abcde','sdaklfj','asdjf','na','basdn']
#matchingStrings(stringList, queries)

def cookies(k , a):

    first_min = 0
    second_min = 0
    a.sort()
    index = 0
    for index in range(len(a)):
        first_min = a[0]
        second_min = a[1]
        if first_min >= k:
            return index

        num = first_min * 1 + second_min * 2
        
        del a[0]
        del a[0]
        a.append(num)
        a.sort()
    return -1

k = 9
a = [2,7,3,6,4,6]
print(cookies(k , a))

