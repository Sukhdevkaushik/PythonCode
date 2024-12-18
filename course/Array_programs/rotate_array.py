def rotate_array(arr, d):
    l = len(arr)
    d = d % l  # Normalize d

    def reverse(arr, left, right):
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    
    reverse(arr, 0, d -1)
    reverse(arr, d, l -1)
    reverse(arr, 0, l -1)
    return arr

# Example usage
#arr = [7,3,9,1]
#rotate_array(arr, 9)
#print(arr)  # Output: [3, 4, 5, 1, 2]
# 
from math import gcd
def rotate_left_juggling(arr, k):
    import pdb; pdb.set_trace()
    n = len(arr)
    k = k % n  # Handle cases where k > n
    
    num_sets = gcd(n, k)  # Find the GCD of n and k
    
    for i in range(num_sets):  # Loop through each set
        temp = arr[i]  # Store the first element of the set
        curridx = i
        
        while True:
            next_idx = (curridx + k) % n  # Calculate the next index
            if next_idx == i:  # End of the cycle
                break
            arr[curridx] = arr[next_idx]  # Move the element to the current position
            curridx = next_idx
        
        arr[curridx] = temp  # Place the stored element in its correct position
    
    return arr

# Example usage:
arr = [1, 2, 3, 4, 5]
k = 2
print("Array after left rotation:", rotate_left_juggling(arr, k))
