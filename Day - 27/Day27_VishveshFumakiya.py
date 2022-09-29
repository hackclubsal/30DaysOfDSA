class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    def print(self):
        ptr = self
        while ptr:
            print(ptr.data, end=' —> ')
            ptr = ptr.next

def reverseInGroups(head, k):
    if head is None:
        return None
    current = head
    prev = None
    count = 0
    while current and count < k:
        count = count + 1
        next = current.next
        current.next = prev
        prev = current
        current = next
    head.next = reverseInGroups(current, k)
    return prev

head = None
for i in reversed(range(9)):
    head = Node(i + 1, head)
 
head = reverseInGroups(head, 3)
head.print()
