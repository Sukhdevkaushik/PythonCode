def find_duplicates(lst):
    seen = set()
    duplicate = set()

    for item in lst:
        if item in seen:
            duplicate.add(item)
        else:
            seen.add(item)
    return duplicate

lst = [1, 2, 3, 4, 2, 5, 1, 6, 7, 3]
print(find_duplicates(lst))
