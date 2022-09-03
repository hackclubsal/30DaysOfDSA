import java.util.Scanner;
import java.util.Arrays;

class Main
{

  public static void sortBinaryArray(int[]array, int n)
  {
    int k = 0;
    for (int i = 0; i < n; i++)
		if (array[i] == 0)
	    	array[k++] = 0;
    for (int i = k; i < n; i++)
		array[k++] = 1;
  }

  public static void main(String[]args)
  {
    int n;
    Scanner scan = new Scanner(System.in);
    System.out.println("Enter the number of array elements: ");
    n = scan.nextInt();
    int[] array = new int[n];
    System.out.println("Enter the array elements: ");
    for (int i = 0; i < n; i++)
    	array[i] = scan.nextInt ();
    sortBinaryArray (array, n);
    System.out.println("Sorted Binary array is: ");
    for (int i = 0; i < n; i++)
    	System.out.print (array[i] + " ");
  }
}