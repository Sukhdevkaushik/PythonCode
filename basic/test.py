# Function to reverse a list without using inbuilt methods
def reverse_list(input_list):
    # Check if the input list is empty
    if not input_list:
        return []
    
    # Create an empty list to store the reversed elements
    reversed_list = []
    
    # Iterate through the original list from end to start
    dat = (len(input_list) - 1, -1, -1)
    print(dat)

    for i in range(len(input_list) - 1, -1, -1):
        # Append each element to the reversed list
        print(i)
        reversed_list.append(input_list[i])
    
    return reversed_list

# Example usage
my_list = [1, 2, 5, 10, 15, 24]
empty_list = []
reversed_list = reverse_list(my_list)
reversed_empty_list = reverse_list(empty_list)

print("Original list:", my_list)
print("Reversed list:", reversed_list)
print("Original empty list:", empty_list)
print("Reversed empty list:", reversed_empty_list)
