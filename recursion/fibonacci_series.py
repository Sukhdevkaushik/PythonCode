def fibonacci_series(n):
    """ """

    if (n == 1):
        return 1
    elif (n == 0):
        return 0
    #elif (n == 2):
    #    return 1
    #if n <= 1:
    #    return n  
    else:
        print("first funcation call " + str(n) + " second funcation " + str(n - 2))
        return (fibonacci_series(n - 1) + fibonacci_series(n - 2))

n = 10
for i in range(n):
    print(fibonacci_series(i), end= " ")