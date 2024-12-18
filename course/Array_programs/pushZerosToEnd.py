def pushZerosToEnd(arr):
	if len(arr) < 2:
		return arr
	left= 0
	right= len(arr) - 1
	while left < right:
		
		if arr[right] == 0:
			right -= 1
		elif arr[right] != 0 and arr[left] ==0:
			arr[right], arr[left] = arr[left], arr[right]			 
			right -= 1
			left += 1		
		else:
			left += 1
		print(arr)
	return arr

#arr = [3, 5, 0, 0, 4]
#print(pushZerosToEnd(arr))

def pushZerosToEnd_2(arr):
	if len(arr) < 2:
		return arr	
	prev_value = 0
	for i in range(len(arr)):		
		if arr[i] != 0:
			arr[i], arr[prev_value]  = arr[prev_value], arr[i]
			prev_value += 1
	return arr

arr = [3, 5, 0, 0, 4]
print(pushZerosToEnd_2(arr))

