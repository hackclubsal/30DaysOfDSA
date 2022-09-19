// Q.15) Given 2 sorted arrays, return the intersection of both the arrays. The intersection of 2 arrays means all the elements which are present in both.
// Example:

// Input:

// Array 1: [1, 3, 4, 5, 5, 6, 6, 7]
// Array 2: [2, 5, 6, 6, 7, 8]
// Output:

// Intersection: [5, 6, 6, 7]

import java.util.ArrayList;

public class Intersect_of_sortedArray {

	public static void main(String[] args) {

		int[] A = {1, 3, 4, 5, 5, 6, 6, 7};
		int[] B = {2, 5, 6, 6, 7, 8};
		
		ArrayList<Integer> ans = intersect(A, B);
	
		System.out.println(ans);
	}
	
	 public static ArrayList<Integer> intersect(final int[] A, final int[] B) {
		    
		    int n=A.length;
		    int m=B.length;
		    ArrayList<Integer> ans = new ArrayList<Integer>();

		    int i=0,j=0;
		    while(i<=n-1 && j<=m-1) {
		    	if(A[i]<B[j]) {
		    		i++;
		    	}
		    	if(A[i]>B[j]) {
		    		j++;
		    	}
		    	if(A[i]==B[j]) {
		    		ans.add(A[i]);
		    		i++;
		    		j++;
		    	}
		    }
		    return ans;
	 }
}
	