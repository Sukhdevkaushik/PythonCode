def find_mean(arr):
    """ """
    total_len = len(arr)
    total_sum = sum(arr)
    mean_num = total_sum / total_len
    print(round(mean_num))


arr = [2, 3, 4, 5 ,7]
find_mean(arr)