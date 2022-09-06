import java.util.Scanner;

public class Day5_AkashRChandran {
	public static void search(int[] array, int low, int high) {
		if (low > high)
			return;
		if (low == high) {
			System.out.println("The required element is " + array[low]);
			return;
		}
		int mid = (low + high) / 2;
		if (mid % 2 == 0) {
			if (array[mid] == array[mid + 1])
				search(array, mid + 2, high);
			else
				search(array, low, mid);
		}
		else if (mid % 2 == 1) {
			if (array[mid] == array[mid - 1])
				search(array, mid + 1, high);
			else
				search(array, low, mid - 1);
		}
	}
	public static void main(String[] args) {
		int n;
		Scanner scan = new Scanner(System.in);
		System.out.print("Enter the number of elements: ");
		n = scan.nextInt();
		int[] array = new int[n];
		System.out.println("Enter the elements of array: ");
		for (int j = 0; j < n; j++)
			array[j] = scan.nextInt();
		search(array, 0, n - 1);
		scan.close();
	}
}