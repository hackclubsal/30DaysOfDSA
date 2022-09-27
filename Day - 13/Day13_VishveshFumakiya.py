class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
 
def leftView(root, level=1, last_level=0):
    if root is None:
        return last_level
 
    if last_level < level:
        print(root.key, end=' ')
        last_level = level
        
    last_level = leftView(root.left, level + 1, last_level)
    last_level = leftView(root.right, level + 1, last_level)
 
    return last_level

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.left.left = Node(7)
root.right.left.right = Node(8)
leftView(root)
