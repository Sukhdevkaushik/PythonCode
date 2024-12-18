class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else: 
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        temp = self.root
        while (temp is not None):
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False
        
    def __r_contains(self, current_node, value):
        if current_node == None: 
            return False      
        if value == current_node.value:
            return True 
        if value < current_node.value:
            return self.__r_contains(current_node.left, value) 
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)


    def r_contains(self, value):
        return self.__r_contains(self.root, value)
    
    def _inorder(self, current_node):
        if current_node:
            self._inorder(current_node.left)
            print(current_node.value, end=' ')
            self._inorder(current_node.right)
    
    def inorder(self):
        self._inorder(self.root)


    def min_value(self, current_node):
        while current_node is not None:
            current_node = current_node.left
        return current_node.value
        

    def _delete_node(self, current_node, value):
        if current_node == None:
            return None
        if value < current_node.value:
            current_node.left = self._delete_node(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self._delete_node(current_node.right, value)
        else:
            if current_node.left == None and current_node.right == None:
                return None
            elif current_node.left == None:
                current_node = current_node.right
            elif current_node.right == None:
                current_node = current_node.right
            else:
                min_tree_value = self.min_tree_value(current_node)
                current_node.right = self._delete_node(current_node.right, min_tree_value)    
        return current_node
        
    def delete_node(self, value):
        self._delete_node(self.root, value)        

my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(20)
my_tree.insert(19)
my_tree.inorder()
print('BST delete 21:')
my_tree.delete_node(21)
my_tree.inorder()

                


"""
    EXPECTED OUTPUT:
    ----------------
    BST Contains 27:
    True

    BST Contains 17:
    False

"""