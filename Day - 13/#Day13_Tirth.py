class Node: 
  def __init__(self, data): 
    self.data = data 
    self.left = None
    self.right = None
  
  
# Recursive function to print left view of a binary tree.
# It takes a root, the current level, and 
# the max level so far of the binary tree
def leftViewUtil(root, level, max_level): 
  if root is None: 
    return

  if (max_level[0] < level): 
    print ("% d " %(root.data)), 
    max_level[0] = level 

  leftViewUtil(root.left, level + 1, max_level) 
  leftViewUtil(root.right, level + 1, max_level) 
  
def leftView(root): 
  max_level = [0] 
  leftViewUtil(root, 1, max_level) 
  
  
# Driver program to test above function 
root = Node(1) 
root.left = Node(2); 
root.right = Node(3); 
root.left.left = Node(4);
root.left.right = Node(5);
root.left.right.left = Node(7);
root.right.left = Node(6);
root.right.left.left = Node(8);
  
leftView(root) 
