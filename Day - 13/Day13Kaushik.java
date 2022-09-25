/*Q.13) There are different ways to look at a binary tree. The left view of a binary tree contains the set of nodes that will be visible if you look at the binary tree from the left side.
Given the root node of a binary tree, return an array containing the node elements in the left view, from top to bottom.

Output:

Print the left-view-binary-tree
See the Example in picture*/


class Node {
	int data;
	Node left, right;

	public Node(int item) {
		data = item;
		left = right = null;
	}
}

class BinaryTree {
	Node root;
	static int max_level = 0;
	void leftViewUtil(Node node, int level) {
		if (node == null)
			return;
		if (max_level < level) {
			System.out.print(" " + node.data);
			max_level = level;
		}

		leftViewUtil(node.left, level + 1);
		leftViewUtil(node.right, level + 1);
	}
	void leftView() {
		max_level = 0;
		leftViewUtil(root, 1);
	}
}

public class Day13Kaushik {
	public static void main(String args[]) {
		BinaryTree tree = new BinaryTree();
		tree.root = new Node(1);
		tree.root.left = new Node(2);
		tree.root.right = new Node(3);
		tree.root.left.left = new Node(4);
		tree.root.left.right = new Node(5);
		tree.root.left.right.left = new Node(7);
		tree.root.right.left = new Node(6);
		tree.root.right.left.left = new Node(8);
		tree.leftView();
	}
}