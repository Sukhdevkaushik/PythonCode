def print_num(n):
    """ """
    if n > 0:
        print(n, end=" ")
        print_num(n - 1)

print_num(10)
