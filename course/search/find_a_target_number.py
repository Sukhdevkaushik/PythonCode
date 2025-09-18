# Function to search how many times 'target' appears in the sorted array 'arr'
def search(arr, target):

    # Helper function to find the first occurrence of the target in the array
    def search_first(arr, target):
        low = 0                      # Initialize low pointer to start of array
        high = len(arr) - 1         # Initialize high pointer to end of array
        
        while low <= high:          # Continue binary search while valid range exists
            mid = low + (high - low) // 2  # Calculate the middle index safely
            if arr[mid] < target:         # If middle element is less than target
                low = mid + 1             # Move low pointer to the right
            elif arr[mid] > target:       # If middle element is greater than target
                high = mid - 1            # Move high pointer to the left
            else:
                # If target found, check if it's the first occurrence
                if mid == 0 or arr[mid - 1] != target:
                    return mid            # Return index if it's the first occurrence
                high = mid - 1            # Otherwise, keep searching in the left half
        return -1                         # Target not found

    # Helper function to find the last occurrence of the target in the array
    def search_last(arr, target):
        low = 0                      # Initialize low pointer to start of array
        high = len(arr) - 1         # Initialize high pointer to end of array
        
        while low <= high:          # Continue binary search while valid range exists
            mid = low + (high - low) // 2  # Calculate the middle index safely
            if arr[mid] < target:         # If middle element is less than target
                low = mid + 1             # Move low pointer to the right
            elif arr[mid] > target:       # If middle element is greater than target
                high = mid - 1            # Move high pointer to the left
            else:
                # If target found, check if it's the last occurrence
                if mid == len(arr) - 1 or arr[mid + 1] != target:
                    return mid            # Return index if it's the last occurrence
                low = mid + 1             # Otherwise, keep searching in the right half
        return -1                         # Target not found

    start = search_first(arr, target)     # Find the index of first occurrence
    if start == -1:                       # If target not found at all
        return 0                          # Return count as 0
    end = search_last(arr, target)       # Find the index of last occurrence
    return end - start + 1               # Total count = last - first + 1

# Example usage:
arr = [1, 2, 2, 2, 2, 3, 3]   # Input sorted array
target = 2                   # Element to count in the array
print(search(arr, target))   # Output the count of target in array
