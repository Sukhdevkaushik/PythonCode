def bubble_sort(lst):
    """ """
    a = 1 
    for i in range(0, len(lst)-1):
        for j in range(len(lst)-1):            
            if lst[j + 1] <= lst[j]:
                elmt = lst[j + 1]
                lst[j + 1] = lst[j]
                lst[j] = elmt
            a = a + 1
            j = j + 1
            i = i + 1
            print(lst)
    return lst

lst = [5, 3, 10, 20, 8, 80]
print(bubble_sort(lst))