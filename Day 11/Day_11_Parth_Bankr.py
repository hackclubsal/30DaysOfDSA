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
        # print(printval.data)

    def toString(self):
        s = ""
        printval = self.head
        while printval is not None:
            s += str(printval.data)
            printval = printval.next
        return int(s)


l1 = LinkedList()
l1.add([9,9,9,9,9,9,9])

l2 = LinkedList()
l2.add([9,9,9,9])

l3 = LinkedList()
l3.add(str(l2.toString() + l1.toString()))
l3.reverse()
l3.printList()