class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        
    def insertion_sort(self):
        if self.length < 2:
            return
            
        sorted_head = self.head
        unsorted_head = self.head.next
        sorted_head.next = None
        
        while unsorted_head is not None:
            current = unsorted_head
            unsorted_head = unsorted_head.next
            
            if current.value < sorted_head.value:
                current.next = sorted_head
                sorted_head = current
            else:
                search_point = sorted_head
                while search_point.next is not None and current.value > search_point.next.value:
                    search_point = search_point.next
                current.next = search_point.next
                search_point.next = current
                
        self.head = sorted_head
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        self.tail = temp
                


my_linked_list = LinkedList(4)
my_linked_list.append(2)
my_linked_list.append(6)
my_linked_list.append(5)
my_linked_list.append(1)
my_linked_list.append(3)

print("Linked List Before Sort:")
my_linked_list.print_list()
my_linked_list.insertion_sort()
print("\nSorted Linked List:")
my_linked_list.print_list()



"""
    EXPECTED OUTPUT:
    ----------------
    Linked List Before Sort:
    4
    2
    6
    5
    1
    3

    Sorted Linked List:
    1
    2
    3
    4
    5
    6

"""

