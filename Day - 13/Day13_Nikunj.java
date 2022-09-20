// Q.13) There are different ways to look at a binary tree. The left view of a binary tree contains the set of nodes that will be visible if you look at the binary tree from the left side.
// Given the root node of a binary tree, return an array containing the node elements in the left view, from top to bottom.

// Output:

// Print the left-view-binary-tree
// See the Example in picture

package Binary_tree;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Binary_Tree{
	
	Scanner sc;
	TreeNode root;
	public Binary_Tree() {
		sc=new Scanner(System.in);
	}
	
	TreeNode createBinaryTree_leet() {
		System.out.println("Enter node data");
		int data = sc.nextInt();
		
		if(data==-1) return null;
		
		TreeNode node = new TreeNode(data);
		System.out.println("Enter "+data +"'s left data");
		node.left = createBinaryTree_leet();
		System.out.println("Enter "+data +"'s right data");
		node.right = createBinaryTree_leet();
		
		return node;
	}
	
		
	
}

//  Definition for a binary tree node.
class TreeNode {
      int val;
      TreeNode left;
      TreeNode right;
      TreeNode() {}
      TreeNode(int val) { this.val = val; }
      TreeNode(int val, TreeNode left, TreeNode right) {
          this.val = val;
          this.left = left;
          this.right = right;
      }
      
  }
 
public class Left_side_view {

	public static void main(String[] args) {
		Binary_Tree btree = new Binary_Tree();
		TreeNode root = btree.createBinaryTree_leet();
		
		List<Integer> ans = leftSideView(root);
		System.out.println(ans);
	}

	 public static List<Integer> leftSideView(TreeNode root) {
			ArrayList<Integer> ans = new ArrayList<>();
			int level=0;
			leftSideView(root,level,ans);
			return ans; 
		 }

		private static void leftSideView(TreeNode root, int level, ArrayList<Integer> ans) {
			if(root==null) return;
			
			if(ans.size()==level) {
				ans.add(root.val);
			}
			
			leftSideView(root.left,level+1,ans);
			leftSideView(root.right,level+1,ans);
			
		}
		
}