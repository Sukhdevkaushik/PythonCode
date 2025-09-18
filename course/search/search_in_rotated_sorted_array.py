# Function to search for 'key' in a rotated sorted array 'arr'
def search(arr, key):
    low = 0                      # Initialize the low pointer at the start of the array
    high = len(arr) - 1         # Initialize the high pointer at the end of the array

    # Binary search loop
    while low <= high:
        mid = (high + low) // 2  # Calculate the middle index

        if arr[mid] == key:
            return mid           # Key found at mid index, return it

        # Check if the left half is sorted
        if arr[low] <= arr[mid]:
            # If key lies in the sorted left half
            if arr[low] <= key < arr[mid]:
                high = mid - 1   # Narrow search to left half
            else:
                low = mid + 1    # Search in right half
        else:
            # If the right half is sorted
            if arr[mid] < key <= arr[high]:
                low = mid + 1    # Narrow search to right half
            else:
                high = mid - 1   # Search in left half

    return -1  # Key not found in array

# Example usage
arr = [5, 6, 7, 8, 9, 10, 1, 2, 3]  # Rotated sorted array
key = 3                             # Element to search for
print(search(arr, key))            # Output the index of the key (should be 8)

# Steps to Implement Modified Binary Search:

# 1. Initialize Pointers:
#    Start with two pointers:
#    - low set to 0
#    - high set to the length of the array minus one

# 2. Binary Search with Modifications:
#    - Calculate the middle index (mid)
#    - Check if the middle element is the target
#      - If yes, return the index
#    - Determine which half of the array is properly sorted:

#      - If the left half (from low to mid) is sorted:
#        - Check if the target lies within this range
#          - If yes, adjust the high pointer to narrow the search to this half
#            (high = mid - 1)
#          - Otherwise, search in the other half by adjusting the low pointer
#            (low = mid + 1)

#      - If the right half (from mid to high) is sorted:
#        - Check if the target lies within this range
#          - If yes, adjust the low pointer to narrow the search to this half
#            (low = mid + 1)
#          - Otherwise, search in the other half by adjusting the high pointer
#            (high = mid - 1)

# 3. Repeat the process until low is less than or equal to high

# 4. Exit Condition:
#    If the loop exits without finding the target,
#    return -1 as the target is not in the array
