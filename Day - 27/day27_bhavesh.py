class Node:
  
    
    def __init__(self, data):
        self.data = data
        self.next = None
  
  
class LinkedList:
  
    
    def __init__(self):
        self.head = None
  
    def reverse(self, head, k):
        
        if head == None:
          return None
        current = head
        next = None
        prev = None
        count = 0
  
        
        while(current is not None and count < k):
            next = current.next
            current.next = prev
            prev = current
            current = next
            count += 1
  
        
        
        
        
        if next is not None:
            head.next = self.reverse(next, k)
  
        
        return prev
  
    
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
  
    
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data,end=' ')
            temp = temp.next
  
  

llist = LinkedList()
llist.push(9)
llist.push(8)
llist.push(7)
llist.push(6)
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)
  
print("Input")
llist.printList()
llist.head = llist.reverse(llist.head, 3)
  
print ("\nOutput")
llist.printList()
