//Q.11) You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
//You may assume the two numbers do not contain any leading zero, except the number 0 itself.

//Example-1:

//Input: l1 = [2,4,3], l2 = [5,6,4]
//Output: [7,0,8]
//Explanation: 342 + 465 = 807.

//Example-2:

//Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
//Output: [8,9,9,9,0,0,0,1]

public class day11_Nikunj {
	public static void main(String args[]) {
		ListNode_dsa m1 = new ListNode_dsa(2);
		ListNode_dsa m2 = new ListNode_dsa(4);
		ListNode_dsa m3 = new ListNode_dsa(3);
			
		ListNode_dsa n1 = new ListNode_dsa(5);
		ListNode_dsa n2 = new ListNode_dsa(6);
		ListNode_dsa n3 = new ListNode_dsa(4);

		ListNode_dsa head1 = m1;
		m1.next=m2;
		m2.next=m3;
		
		ListNode_dsa head2 = n1;
		n1.next=n2;
		n2.next=n3;

		System.out.print("LL1: ");
		printLL(head1);

		System.out.print("LL2: ");
		printLL(head2);

		System.out.print("ans: ");
		ListNode_dsa sum = sum(head1,head2);
		printLL(sum);
	}
	private static ListNode_dsa sum(ListNode_dsa head1, ListNode_dsa head2) {
		ListNode_dsa head = null,tail = null;
		int carry = 0;
		while(head1!=null || head2!=null || carry==1) {
			int sum=carry;
			if(head1!=null) {
				sum+=head1.val;
				head1=head1.next;
			}
			if(head2!=null) {
				sum+=head2.val;
				head2=head2.next;				
			} 
			
			int digit = sum%10;
			carry = sum/10;
			
			ListNode_dsa newNode = new ListNode_dsa(digit);
			if(head==null){
                head=newNode;
                tail=newNode;    
            } 
            else {
				tail.next = newNode;
				tail = newNode;
			}
		}
		return head;
	}
	static void printLL(ListNode_dsa head) {
		ListNode_dsa cur = head;
		while(cur!=null) {
			System.out.print(cur.val+" -> ");
			cur=cur.next;
		}
		System.out.println("End");
	}

}
	
class ListNode_dsa{
	int val;
	ListNode_dsa next;

	ListNode_dsa(int val) {
		this.val = val;
	}

	ListNode_dsa(int val, ListNode_dsa next) {
		this.val = val;
		this.next = next;
	}
	
}
