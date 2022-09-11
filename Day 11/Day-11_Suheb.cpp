#include <bits/stdc++.h>
using namespace std;

struct ListNode
{
    int val;
    ListNode *next;
    ListNode(int v)
    {
        val = v;
        next = NULL;
    }
};

void insertAtBeginning(ListNode *&head, int data)
{
    ListNode *newNode = new ListNode(data);
    newNode->next = head;
    head = newNode;
}

ListNode* addTwoNumbers(ListNode* head1, ListNode* head2)
{
    ListNode *dummy = new ListNode(-1);
    ListNode *prevNode = dummy;
    int sum = 0, carry = 0;
    while (head1 != NULL || head2 != NULL)
    {
        int digit1 = 0, digit2 = 0;
        if (head1 != NULL)
        {
            digit1 = head1->val;
            head1 = head1->next;
        }
        if (head2 != NULL)
        {
            digit2 = head2->val;
            head2 = head2->next;
        }
        sum = digit1 + digit2 + carry;
        carry = sum / 10;
        prevNode->next = new ListNode(sum % 10);
        prevNode = prevNode->next;
    }
    if (carry != 0)
        prevNode->next = new ListNode(carry);
    ListNode *res = dummy->next;
    delete dummy;
    return res;
}

void printList(ListNode *head)
{
    while (head != NULL)
    {
        cout << " " << head->val;
        head = head->next;
    }
    cout << endl;
}

int main()
{
    ListNode *head1 = NULL, *head2 = NULL;
    insertAtBeginning(head1, 3); // 3
    insertAtBeginning(head1, 4); // 4->3
    insertAtBeginning(head1, 2); // 2->4->3

    insertAtBeginning(head2, 4); // 4
    insertAtBeginning(head2, 6); // 6->4
    insertAtBeginning(head2, 5); // 5->6->4

    cout << "Number 1:";
    printList(head1);
    cout << "Number 2:";
    printList(head2);

    cout << "Number after addition:";
    ListNode *res = addTwoNumbers(head1, head2);
    printList(res);
    return 0;
}