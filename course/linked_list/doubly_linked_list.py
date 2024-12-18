class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class Doublylinkedlist:
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
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        
        temp = self.tail.prev
        temp.next = None
        temp.prev = None
        self.tail = temp
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = Node

    def prepend(self, value):
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node = Node(value)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return False
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return True
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp
        
    def set_value(self, index, value):
        if index < 0 or index >= self.length:
            return None        
        temp = self.head
        for _ in range(index):
            temp = temp.next
        temp.value = value

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        
        if  index == 0:
            self.prepend(value)
            return True
        
        if index == self.length:
            self.append(value)
            return True
        
        new_node = Node(value)
        temp = self.head
        for _ in range(index-1):
            temp = temp.next
        next_value = temp.next
        temp.next = new_node
        new_node.prev = temp
        new_node.next = next_value
        next_value.prev = new_node
        self.length += 1
        return True
    
    def remove(self, index):
        if index < 0 or index > self.length:
            return None
        
        if  index == 0:
            self.pop_first()
            return True
        
        if index == self.length:
            self.pop()
            return True
        
        temp = self.get(index)
        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        temp.next = None
        temp.prev = None
        self.length -= 1
        return True

my_doubly_linked_list = Doublylinkedlist(7)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.print_list()
print("list before pop_first")
my_doubly_linked_list.remove(1)

my_doubly_linked_list.print_list()
print("list after pop_first")
