def add_binary(a, b):
    if len(a)<1:
        return b
    if len(b)<1:
        return a
    #max_len = max(len(a), len(b))
    a = a.lstrip('0')
    b = b.lstrip('0')

    carry = 0
    i, j = len(a) - 1, len(b) - 1
    result = []
    while i >= 0 or j >= 0 or carry:
        digita = int(a[i]) if i >=0 else 0
        digitb = int(b[j]) if j >=0 else 0
        total = digita + digitb + carry
        carry = total // 2
        result.append(str(total % 2))
        i -= 1
        j -= 1
        # If there's a carry remaining, add it
    if carry:
        result.append('1')

    return ''.join(result[::-1])
a = "01001001"
b = "0110101"
print(add_binary(a, b))