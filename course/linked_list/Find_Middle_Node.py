class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
    
    def find_middle_node(self):
        """ """
        if self.head and self.head.next == None:
            return self.head
        fast_number = self.head
        slow_number = self.head
        
        while fast_number.next != None:
            temp = fast_number.next
            if temp.next == None:        
                return slow_number.next
            fast_number = temp.next
            slow_number = slow_number.next                            
        return slow_number
    
    def has_Loop(self):
        """ """
        visted = self.head
        temp = self.head
        while temp.next is not None:
            current_node = temp.next
            if current_node 
             

my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
#my_linked_list.append(5)

print( my_linked_list.find_middle_node().value )



"""
    EXPECTED OUTPUT:
    ----------------
    3
    
"""