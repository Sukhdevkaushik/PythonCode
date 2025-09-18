def count_inversions_burte(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                count += 1
    return count



#print(count_inversions_burte(arr))
#===========optimimal soluation==============
def merge(lst1, mid_index, lst2):
    i = 0
    j = 0
    len_lst = len(lst1)
    combined = []
    count = 0
    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            combined.append(lst1[i])
            i += 1
        else:
            combined.append(lst2[j])
            j += 1
            count += len_lst - i

    while i < len(lst1):
        combined.append(lst1[i])
        i += 1

    while j < len(lst2):
        combined.append(lst2[j])
        j += 1
    return combined, count

def count_inversions(arr):
    if len(arr) == 1:
        return arr
    mid_index = len(arr) // 2
    left, left_count = count_inversions(arr[:mid_index])
    right, right_count = count_inversions(arr[mid_index:])
    merged, left_count + right_count = merge(left, mid_index ,right)
    
arr = [2, 4, 1, 3, 5]
print(count_inversions(arr)[1])