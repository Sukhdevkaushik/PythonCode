def fibonacci_series(n):
    """ """
    a, b = 0, 1
    series = []
    for _ in range(n):
        series.append(a)
        b, a = a + b, b
    return series
print(fibonacci_series(10))
