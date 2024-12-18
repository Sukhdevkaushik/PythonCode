class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def print_data(self):
        pass


    def insert(self, value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
            self.root.left = None
            self.root.right = None
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            elif new_node.value > self.root.value:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
            else:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left

    def contains(self, value):
        if self.root == None:
            return False
        temp = self.root
        while temp is not None:
            if value > temp.value:
                temp = temp.right
            elif value < temp.value:
                temp = temp.left
            elif value == temp.value:
                return value
            else:
                return None
            
            
tree = BinarySearchTree()
tree.insert(27)
tree.insert(76)
tree.insert(18)
#print(tree.root.value)
#print(tree.root.left.value)
#print(tree.root.right.value)    
print("check contains method")
print(tree.contains(79))
    