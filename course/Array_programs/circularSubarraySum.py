def circularSubarraySum(arr):
        """ """
        curr_min = arr[0]
        min_sum = arr[0]
        curr_max = arr[0]
        max_sum = arr[0]
        total_sum = arr[0]
        if len(arr) < 2 and arr != None:
            return arr[0]
        
        for i in range(1, len(arr)):
            #current min         
            curr_min = min(arr[i], curr_min + arr[i])
            min_sum = min(min_sum, curr_min)
            #current max
            curr_max = max(arr[i], curr_max + arr[i])
            max_sum = max(max_sum, curr_max)
            #total sum
            total_sum += arr[i]

        # Handle case where all numbers are negative
        if max_sum < 0:
            return max_sum  
    
        return max(max_sum, total_sum - min_sum)