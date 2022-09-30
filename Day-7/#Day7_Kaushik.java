public class Main {

	public static void main(String[] args) {
		ListNode n1 = new ListNode(10);
		ListNode n2 = new ListNode(20);
		ListNode n3 = new ListNode(30);
		ListNode n4 = new ListNode(40);
		ListNode n5 = new ListNode(50);
		ListNode n6 = new ListNode(60);
		

		ListNode head = n1;
		n1.next=n2;
		n2.next=n3;
		n3.next=n4;
		n4.next=n5;
		n5.next=n6;
		
		printLL(head);
		
		System.out.println("Reverse linkedlist: ");
		
		ListNode ans = reverse(head);
		printLL(ans);
	}
	
	private static ListNode reverse(ListNode head) {
		ListNode cur =head;
		ListNode prev =null;
		
		while(cur!=null) {
			ListNode temp=cur.next;
			cur.next=prev;
			prev=cur;
			cur=temp;
		}
		return prev;
	}

	static void printLL(ListNode head) {
		ListNode cur = head;
		while(cur!=null) {
			System.out.print(cur.data+" -> ");
			cur=cur.next;
		}
		System.out.println("End");
	}


}

class ListNode {
	int data;
	ListNode next;

	public ListNode(int data) {
		this.data = data;
	}
