def top_k_the_frequency(words, k):
    ''''''
    result = {}
    r = []
    for string in words:
        result[string] = result.get(string, 0) + 1

    for key, value in result.items():
        if value >= k:
            r.append(key)
    return r

words = ["i","love","leetcode","i","love","coding"] 
k = 2
print(top_k_the_frequency(words, k))

