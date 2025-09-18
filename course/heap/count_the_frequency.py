def count_the_frequency(my_list):
    count = {}
    for item in my_list:
        if item in count:
            count[item] += 1
        else:
            count[item] = 1
    return count

my_list = [1, 2, 2, 3, 1, 4, 2, 1]
print(count_the_frequency(my_list))