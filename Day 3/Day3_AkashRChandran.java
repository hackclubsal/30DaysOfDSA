import java.util.Scanner;

public class Day3_AkashRChandran {

	public static boolean searchMatrix(int[][] matrix, int m, int n, int key) {
		for (int i = 0; i < m; i++)
			for (int j = 0; j < m; j++)
				if (matrix[i][j] == key) 
					return true;
		return false;
	}
	public static void main(String args[]) {
		int m, n, key;
		Scanner scan = new Scanner(System.in);
		System.out.print("Enter the number of rows: ");
		m = scan.nextInt();
		System.out.print("Enter the number of columns: ");
		n = scan.nextInt();
		int[][] matrix = new int[m][n];
		System.out.println("Enter the elements of matrix: ");
		for (int i = 0; i < m; i++)
			for (int j = 0; j < n; j++)
				matrix[i][j] = scan.nextInt();
		System.out.print("Enter the key to search: ");
		key = scan.nextInt();
		System.out.print("The key exits: ");
		System.out.println(searchMatrix(matrix, m, n, key));
		scan.close();
	}
}
