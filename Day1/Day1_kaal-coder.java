//Kaushik Lakhani
//Day1
import java.util.Arrays;
public class Main
{
    // Function to sort binary array
    public static void sort(int[] A)
    {
        // count number of 0's
        int zeros = 0;
        for (int value: A)
        {
            if (value == 0) {
                zeros++;
            }
        }
         // put 0's at the beginning
        int k = 0;
        while (zeros-- != 0) {
            A[k++] = 0;
        }
         // put 1's at the ending
        while (k < A.length) {
            A[k++] = 1;
        }
    }
 
    public static void main (String[] args)
    {
        int[] A = { 1, 0, 1, 0, 1, 0, 0, 1 };
 
        sort(A);
 
        // print the sorted array
        System.out.println(Arrays.toString(A));
    }
}