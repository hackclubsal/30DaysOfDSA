# Print the left-view-binary-tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def leftView(self):
        if self.root is None:
            return
        queue = []
        queue.append(self.root)
        while queue:
            n = len(queue)
            for i in range(1, n+1):
                temp = queue.pop(0)
                if i == 1:
                    print(temp.data, end=" ")
                if temp.left is not None:
                    queue.append(temp.left)
                if temp.right is not None:
                    queue.append(temp.right)

if __name__ == "__main__":
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.right = Node(4)
    tree.root.left.right.right = Node(5)
    tree.root.left.right.right.right = Node(6)
    tree.leftView()