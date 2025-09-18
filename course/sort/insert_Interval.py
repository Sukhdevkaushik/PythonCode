def overlapping_intervals(arr, newinterval):
	if arr == None:
		return arr
	res = []
	i =0
	n = len(arr)
	while  i < n and arr[i][1] < newinterval[0]:
		res.append(arr[i])
		i += 1
	while i < n and arr[i][0] <= newinterval[1]:
		newinterval[0] = min(newinterval[0], arr[i][0])
		newinterval[1] = max(newinterval[1], arr[i][1])
		i += 1
	res.append(newinterval)

	while i < n:
		res.append(arr[i])
		i += 1
	return res


arr =   [[0, 137], [141,153], [157, 207], [236, 240]]
newinterval = [45,75]
#arr.append(newinterval)
print(overlapping_intervals(arr, newinterval))