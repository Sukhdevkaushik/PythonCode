def reversed(lst):
    """ """
    if len(lst)<= 1:
        return lst
    
    data = []
    i = 0
    l_elmt = len(lst)

    for value in range(int((len(lst)/2) + 1)):
        back_num = lst[l_elmt -1]
        lst[l_elmt -1] = value
        lst[i] = back_num
        i = i + 1
        l_elmt = l_elmt - 1
        print(lst)

    return lst

lst = [4, 5, 6, 7, 8, 9]
print(lst)
print(reversed(lst))