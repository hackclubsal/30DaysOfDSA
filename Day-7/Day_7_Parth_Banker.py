from asyncio.windows_events import NULL
from tkinter.messagebox import NO


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
 
 
class LinkedList:
    def __init__(self):
        self.head = None

    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def add(self, l):
        for new_data in l:
            if self.head is None:
                self.head = Node(new_data)
            else:
                new_node = Node(new_data)
        
                last = self.head

                while (last.next):
                    last = last.next

                last.next = new_node

    def printList(self):
        printval = self.head
        while printval is not None:
            print(printval.data, end=" ")
            printval = printval.next

l1 = LinkedList()
l1.add([1,2,3,4,5])
l1.reverse()
l1.printList()