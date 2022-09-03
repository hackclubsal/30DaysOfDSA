public class Main{
	public static void main(String[] args){
		int[][] matrix = {
				{1,2,3},
				{4,5,6},
				{7,8,9}
		}; 
		int target = 6;

		System.out.println(searchMatrix(matrix,target));

	};

	static boolean searchMatrix(int[][] matrix, int target) {
		for (int row = 0; row<matrix.length; row++){
			for(int col = 0; col<matrix[row].length; col++){
				if (target == matrix[row][col]){
					return true;
				}
			}
		}return false;
	}
}