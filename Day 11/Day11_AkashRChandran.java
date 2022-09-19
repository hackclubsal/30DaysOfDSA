class ListNode {
	int val;
	ListNode next;
	ListNode() {
	}
	ListNode(int val) {
		this.val = val;
	}
	ListNode(int val, ListNode next) {
		this.val = val;
		this.next = next;
	}
}

public class Day11_AkashRChandran {
	static ListNode addTwoNumbers(ListNode l1, ListNode l2) {
		ListNode head = null;
		ListNode temp = null;
		int carry = 0;
		while (l1 != null || l2 != null) {
			int sum = carry;
			if (l1 != null) {
				sum += l1.val;
				l1 = l1.next;
			}
			if (l2 != null) {
				sum += l2.val;
				l2 = l2.next;
			}
			ListNode node = new ListNode(sum % 10);
			carry = sum / 10;
			if (temp == null) {
				temp = head = node;
			} else {
				temp.next = node;
				temp = temp.next;
			}
		}
		if (carry > 0) {
			temp.next = new ListNode(carry);
		}
		return head;
	}

	static void display(ListNode head) {
		ListNode ptr = head;
		while(ptr != null) {
			System.out.print(ptr.val);
			ptr=ptr.next;
		}
	}
	public static void main(String[] args) {
		ListNode n1 = new ListNode(2);
		ListNode n2 = new ListNode(4);
		ListNode n3 = new ListNode(3);
		ListNode m1 = new ListNode(5);
		ListNode m2 = new ListNode(6);
		ListNode m3 = new ListNode(4);
		ListNode head1 = m1;
		m1.next=m2;
		m2.next=m3;

		ListNode head2 = n1;
		n1.next=n2;
		n2.next=n3;

		ListNode sum = addTwoNumbers(head1, head2);
		System.out.print("Sum is equal to: ");
		display(sum);
	}
}
