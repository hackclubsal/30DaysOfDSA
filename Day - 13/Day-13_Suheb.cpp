#include <bits/stdc++.h>
using namespace std;

struct Node
{
 int data;
 struct Node *left, *right;
};

struct Node *newNode(int item)
{
 struct Node *temp = (struct Node *)malloc(sizeof(struct Node));
 temp->data = item;
 temp->left = temp->right = NULL;
 return temp;
}

void leftViewUtil(struct Node *root,
    int level, int *max_level)
{
 if (root == NULL) return;

 if (*max_level < level)
 {
  cout << root->data << " ";
  *max_level = level;
 }

 leftViewUtil(root->left, level + 1, max_level);
 leftViewUtil(root->right, level + 1, max_level);
 
}

void leftView(struct Node *root)
{
 int max_level = 0;
 leftViewUtil(root, 1, &max_level);
}

int main()
{
 Node* root = newNode(1);
 root->left = newNode(2);
 root->right = newNode(3);
 root->left->left = newNode(4);
 root->left->right = newNode(5);
 root->right->left = newNode(6);
 root->left->right->left = newNode(7);
 root->right->left->left = newNode(8);

 leftView(root);

 return 0;
}
