#Reverse the linkedlist
class Node(object):
    def __init__(self, value, next=None): 
        self.value = value                
        self.next = next                  

def reverse(head):
    temp = head
    prev = 0
    while temp is not None:
        prev += 1
        temp = temp.next
    for i in range(prev-1,0,-1):
        xcount = 0
        temp = head
        while (xcount != i):
            temp.value, temp.next.value = temp.next.value, temp.value
            temp = temp.next
            xcount += 1
    return head

def printnodes(n):
    b = True
    while b == True:
        try:
            print(n.value, end = " ")
            n = n.next
        except:
            b = False
    print(" ")

n0 = Node(1,Node(2,Node(3,Node(4,Node(5,)))))
printnodes(n0)

n1 = reverse(n0)
printnodes(n1)
