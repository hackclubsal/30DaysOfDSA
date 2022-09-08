public class Day7_AkashRChandran {
    static LinkedListNode head;

    static class LinkedListNode {
        int val;
        LinkedListNode next;

        LinkedListNode(int no) {
            val = no;
            next = null;
        }
    }

    LinkedListNode reverse(LinkedListNode node) {
        LinkedListNode previous = null;
        LinkedListNode curr = node;
        LinkedListNode next = null;
        while (curr != null) {
            next = curr.next;
            curr.next = previous;
            previous = curr;
            curr = next;
        }
        node = previous;
        return node;
    }

    void printList(LinkedListNode nde) {
        while (nde != null) {
            System.out.print(nde.val + " ");
            nde = nde.next;
        }
    }

    public static void main(String argvs[]) {
        Day7_AkashRChandran listObj = new Day7_AkashRChandran();
        listObj.head = new LinkedListNode(4);
        listObj.head.next = new LinkedListNode(6);
        listObj.head.next.next = new LinkedListNode(7);
        listObj.head.next.next.next = new LinkedListNode(1);
        listObj.head.next.next.next.next = new LinkedListNode(5);
        System.out.println("The Linked list before reversal is: ");
        listObj.printList(head);
        head = listObj.reverse(head);
        System.out.println("\n");
        System.out.println("After reversal, the linked list is: ");
        listObj.printList(head);
    }
}