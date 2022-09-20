## Q.11) You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

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

    def Add(self):
        sum = 0
        temp = self.head
        while temp:
            sum = sum*10 + temp.data
            temp = temp.next
        return sum


if __name__ == "__main__":
    l1 = LinkedList()
    l1.add([2,4,3])
    l2 = LinkedList()
    l2.add([5,6,4])
    print(l1.Add() + l2.Add())
