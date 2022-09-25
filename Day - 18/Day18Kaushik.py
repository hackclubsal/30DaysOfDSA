/*Q.18) A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.
The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

Example-1:

Input: root = [1,2,3]
Output: 6
Explanation:

The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

Example-2:

Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation:

The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.*/


class Node:
   
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
def findMaxUtil(root):
    
    if root is None:
        return 0
    
    l = findMaxUtil(root.left)
    r = findMaxUtil(root.right)
    
    max_single = max(max(l, r) + root.data, root.data)
    
    max_top = max(max_single, l+r+ root.data)
    
    findMaxUtil.res = max(findMaxUtil.res, max_top)
 
    return max_single
 
def findMaxSum(root):
         
    findMaxUtil.res = float("-inf")
         
    findMaxUtil(root)
    return findMaxUtil.res
 

root = Node(1)
root.left = Node(2)
root.right   = Node(3);

print ("Output:" ),findMaxSum(root);