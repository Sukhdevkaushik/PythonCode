def overlapping_intervals(arr):
	if arr == None:
	    return arr
	arr.sort()
	res = []
	res.append(arr[0])
	for i in range(1, len(arr)):
	    last = res[-1]
	    current = arr[i]
	       
	    if current[0] <= last[1]:
	        last[-1] = max(last[1], current[1])
	    else:
	        res.append(current)
	return res


arr =  [[1,3],[2,4],[6,8],[9,10]]
print(overlapping_intervals(arr))