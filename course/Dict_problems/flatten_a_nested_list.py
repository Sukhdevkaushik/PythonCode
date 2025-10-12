def flatten_a_nested_list(lst):
    result = []
    for value in lst:
        if isinstance(value, list):
            result.extend(flatten_a_nested_list(value))
        else:
            result.append(value)
    return result
lst = [1, [2, 5, [3, [4]]]]
 
#print(flatten_a_nested_list(lst))    
from collections import defaultdict
def flatten_a_nested_list(lst):
    result = {}
    for key, value in enumerate(lst):
        if isinstance(value, list):            
            result[key] = flatten_a_nested_list(value)
        else:
            result[key] = value
    return result
lst = [1, [2, 5, [3, [4]]]]
print(flatten_a_nested_list(lst))