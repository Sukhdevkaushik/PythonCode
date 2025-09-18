def second_largest_number(lst):
    first_largest = float('-inf')
    second_largest = float('-inf')
    for item in lst:
        if item > first_largest:
            second_largest, first_largest = first_largest, item
        elif item != first_largest and item > second_largest:
            second_largest = item
    if second_largest == float('inf'):
        return None
    return second_largest

lst = [-12, -35, -1, -10, -34, -1]
print(second_largest_number(lst))


    