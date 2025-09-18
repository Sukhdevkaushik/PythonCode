def noon_overlapping_intervals(arr):
	arr.sort()
	if arr == None:
	    return arr
	count = 0
	arr.sort(key=lambda x: x[1])
	end = arr[0][1]
	
	for i in range(1, len(arr)):
		current = arr[i]		
		if end > current[0]:
			count += 1
			end = min(current[1], end)
		else:
			end  = arr[i][1]
	return count
		


arr =  [[66,135], [26,95], [77,112],[31,52],[15,44], [57,62],[59,118],[25,107],[67,120]]

print(noon_overlapping_intervals(arr))