//Given a matrix, check if the matrix contains a given key.
//The matrix has the following properties:

//Integer in each row is arranged in non-decreasing order from left to right. The first integer in every row is greater than the last integer of the previous row.

//Expected Time Complexity: O(log (n*m))

//Examples:

//Matrix:

//[1 2 3
//4 5 6
//7 8 9]
//Input Key: 6

//Output: Answer - true

public class day3_Nikunj {

	public static void main(String[] args) {
		int[][] mat= {{1,2,3},
						{4,5,6},
						{7,8,9}};
		int key = 6;
		System.out.println(check(mat,key));

	}

	private static boolean check(int[][] mat, int key) {
		int m=mat.length;
		int n=mat[0].length;
		
		for(int i=0;i<m;i++) {
			if(mat[i][n-1]<=key) {
				for(int j=n-1;j>=0;j--) {
					if(mat[i][j]==key) return true;
				}	
			}
		}
		return false;
	}

}
