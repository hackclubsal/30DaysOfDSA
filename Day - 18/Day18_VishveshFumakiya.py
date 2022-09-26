class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Node) -> int:
        self.max_sum = float('-inf')
        self.dfs(root)
        return self.max_sum
    
    def dfs(self, node):
        if not node: return 0
        
        leftST_sum = max(0, self.dfs(node.left))
        rightST_sum = max(0, self.dfs(node.right))
        self.max_sum = max(self.max_sum, leftST_sum + rightST_sum + node.val)
        
        return max(leftST_sum, rightST_sum) + node.val

ob = Solution()
root = Node(1)
root.left = Node(2)
root.right = Node(3)
print(ob.maxPathSum(root))
