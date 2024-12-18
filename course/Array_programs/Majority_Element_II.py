def majority_element_2(arr, n):
    result = []
    check = len(arr) / 3
    for i in range(len(arr)):
        num = arr[i]
        count = 0
        for j in range(len(arr)):
            if num == arr[j]:                
                count += 1
            #print(str(num) +" ka count "+ str(count))
            #print(count / len(arr))
        if count >= check and num not in result:
            result.append(count)
    return result

#arr = [2, 1, 5, 5, 5, 5, 6, 6, 6, 6, 6]
#print(majority_element_2(arr, 3))
#==================================================================

def majority_element_2_batter(arr):
    result = {}
    data = []
    for value in arr:
        if value in result:
            result[value] += 1
        else:
            result[value] = 1
    for key, value in result.items():
        if value >= 3:
            data.append(key)
    return data

#arr = [2, 1, 5, 5, 5, 5, 6, 6, 6, 6, 6]
#print(majority_element_2_batter(arr))
#==================================================================
def majority_element_2_best(arr):
    majority1 = 0
    votes1 = 0
    majority2 = 0
    votes2 = 0

    for value in arr:
        #=======================================
        if votes1 == 0 and value != majority2:
            majority1 = value
            votes1 = 1
        elif votes2 == 0 and value != majority1:
            majority2 = value
            votes2 = 1
        #=======================================
        elif majority1 == value:
            votes1 += 1
        elif majority2 == value:
            votes2 += 1
        #=======================================
        else:
            votes1 -= 1
            votes2 -= 1
        #=======================================
    #Final validation weather value are present or not
    count1 = sum(1 for x in arr if x == majority1)
    count2 = sum(1 for x in arr if x == majority2)
    result = []
    if count1 > len(arr) / 3:
        result.append(majority1)
    if count2 > len(arr) / 3 and majority2 != majority1:
        result.append(majority2)
    # Step 3: Manually sort the result
    if len(result) == 2 and result[0] > result[1]:
        result[0], result[1] = result[1], result[0]  # Swap to ensure ascending order
    return result


arr = [-3, -3, 2, 1, 4, -3]
print(majority_element_2_best(arr))
