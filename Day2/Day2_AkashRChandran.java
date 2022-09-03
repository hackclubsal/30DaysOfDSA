package Day2;

import java.util.Scanner;

class Array_Rotation {

	static void rotate(int array[], int n, int k) {
		k = k % n;
		for (int i = 0; i < n; i++) 
		{
			if (i < k)
				System.out.print(array[n + i - k] + " ");
			else 
				System.out.print(array[i - k] + " ");
		}
	}

	public static void main(String args[]) {
		int n, k;
		Scanner scan = new Scanner(System.in);
		System.out.print("Enter the number of elements in array: ");
		n = scan.nextInt();
		int[] array = new int[n];
		System.out.println("Enter the elements: ");
		for (int i = 0; i < n; i++)
			array[i] = scan.nextInt();
		System.out.print("Enter the steps by which array is to rotated: ");
		k = scan.nextInt();
		rotate(array, n, k);
		scan.close();
	}
}
