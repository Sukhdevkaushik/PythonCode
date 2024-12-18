def plusOne(digits):
    added_value = int("".join([ str(d) for d in digits])) + 1
    return [int(value) for value in str(added_value)]
digits = [8,9,9,9]
print(plusOne(digits))
