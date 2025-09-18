def search_in_rotated_array(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        # Check if the mid element is the target
        if arr[mid] == target:
            return mid
        
        # Determine which half is properly sorted
        if arr[low] <= arr[mid]:  # Left half is sorted
            if arr[low] <= target < arr[mid]:  # Target is in the left half
                high = mid - 1
            else:  # Target is in the right half
                low = mid + 1
        else:  # Right half is sorted
            if arr[mid] < target <= arr[high]:  # Target is in the right half
                low = mid + 1
            else:  # Target is in the left half
                high = mid - 1
    
    return -1  # Target not found

# Example usage
arr = [5, 6, 7, 8, 9, 10, 1, 2, 3]
target = 3
print(search_in_rotated_array(arr, target))  # Output: 8
