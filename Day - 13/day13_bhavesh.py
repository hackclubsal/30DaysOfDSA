class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 

def leftView(root):
    ans = []
 
    if not root:
        return ans
 
    q = []
    q.append(root)
    q.append(None)
    ok = True
 
    while len(q) != 0:
        it = q[0]
        del q[0]
        if it == None:
            if ok == False:
                ok = True
            if len(q) == 0:
                break
 
            else:
                q.append(None)
 
        else:
            if ok:
                ans.append(it.data)
                ok = False
 
            if it.left != None:
                q.append(it.left)
            if it.right != None:
                q.append(it.right)
 
    return ans
 
 

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)
    root.right.left = Node(7)
    root.right.right.left = Node(8)
 
    vec = leftView(root)
 
    
    for x in vec:
        print(x, end=" ")
    print()
