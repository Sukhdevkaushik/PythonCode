class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.hieght = 1

    def print_stack(self):
        """ """
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        """ """
        new_node = Node(value)
        if self.top == None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
            self.hieght += 1

    def pop(self):
        """ """
        if self.hieght == 0:
            return None
        temp = self.top
        self.top = temp.next
        temp.next = None
        self.hieght -= 1


stack = Stack(1)
stack.print_stack()

stack.push(2)
stack.push(3)
stack.print_stack()
print("after push")
stack.pop()
print("after pop")
stack.print_stack()


    