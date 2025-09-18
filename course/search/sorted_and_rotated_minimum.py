# Function to find the minimum number in a rotated sorted array
def find_number(arr):
    low = 0                         # Initialize the low pointer at the start of the array
    high = len(arr) - 1            # Initialize the high pointer at the end of the array

    # If the array is already sorted and not rotated, the smallest element is at the beginning
    if arr[low] < arr[high]:
        return arr[low]

    # Use modified binary search to find the minimum in a rotated sorted array
    while low < high:
        mid = (high + low) // 2    # Calculate the middle index

        # If the middle element is greater than the element at high,
        # the minimum must be in the right half
        if arr[mid] > arr[high]:
            low = mid + 1          # Move the low pointer to the right of mid
        else:
            # Otherwise, the minimum is at mid or in the left half
            high = mid             # Move the high pointer to mid

    # When the loop ends, low == high, which is the index of the minimum element
    return arr[low]

# Example usage
arr = [3, 1, 2]                    # Rotated sorted array
print(find_number(arr))           # Output the minimum element
