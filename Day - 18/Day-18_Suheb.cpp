#include <iostream>
#include <limits>
using namespace std;
 
struct Node
{
    int data;
    Node *left, *right;
 
    Node(int data)
    {
        this->data = data;
        this->left = this->right = nullptr;
    }
};
 
int maxPathSum(Node* node, int &res)
{
    if (node == nullptr) {
        return 0;
    }
 
    int left = maxPathSum(node->left, res);
    int right = maxPathSum(node->right, res);
 
    res = max(res, node->data);
    res = max(res, node->data + left);
    res = max(res, node->data + right);
    res = max(res, node->data + left + right);
 
    return max(node->data, node->data + max(left, right));
}
 
int main()
{
    /* Construct the following tree

           -10
          /   \
         /     \
        9      20
              /  \
             15   7

    */
 
    Node* root = new Node(-10);
    root->left = new Node(9);
    root->right = new Node(20);
    root->right->left = new Node(15);
    root->right->right = new Node(7);
 
    int res = numeric_limits<int>::min();
    maxPathSum(root, res);
    cout << res << endl;
 
    return 0;
}