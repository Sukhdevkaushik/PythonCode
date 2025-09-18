def merge(lst1, lst2):
    i = 0
    j = 0
    combined = []
    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            combined.append(lst1[i])
            i += 1
        else:
            combined.append(lst2[j])
            j += 1

    while i < len(lst1):
        combined.append(lst1[i])
        i += 1

    while j < len(lst2):
        combined.append(lst2[j])
        j += 1
    return combined

def merge_sort(original_list):
    if len(original_list) == 1:
        return original_list
    mid_index = len(original_list) // 2
    left = merge_sort(original_list[:mid_index])
    right = merge_sort(original_list[mid_index:])
    return merge(left, right)



original_list = [3,1,4,2]

sorted_list = merge_sort(original_list)

print('Original List:', original_list)

print('\nSorted List:', sorted_list)