class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
 
    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

class Solution:
    def reverse(self,head):
        if head is None or head.next is None:
            return head
        prev = None
        next = None
        curr = head
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        head = prev
        return head

    def addTwonums(self, first, second):
        curr1 = self.reverse(first)
        curr2 = self.reverse(second)
        sum = 0
        carry = 0
        res = None
        prev = None
        while curr1 is not None or curr2 is not None:
            sum = carry + (curr1.data if curr1 else 0) + (curr2.data if curr2 else 0)
            carry = (1 if sum >= 10 else 0)
            sum = sum % 10
            temp = Node(sum)
            if res is None:
                res = temp
            else:
                prev.next = temp
            prev = temp
            if curr1:
                curr1 = curr1.next
            if curr2:
                curr2 = curr2.next
        if carry > 0:
            temp.next = Node(carry)
        ans = self.reverse(res)
        return ans

def printList(n):
    while n:
        print(n.data, end=' ')
        n = n.next
    print()
    

a1 = [2, 4, 3]
l1 = Linkedlist()
for i in a1:
    l1.insert(i)
a2 = [5, 6, 4]
l2 = Linkedlist()
for i in a2:
    l2.insert(i)

res = Solution().addTwonums(l1.head, l2.head)
printList(res)
