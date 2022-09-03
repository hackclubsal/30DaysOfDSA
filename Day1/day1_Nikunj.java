import java.util.Arrays;

//Sort binary array in linear time.
//Given a binary array, sort it in linear time and constant space. The output should print all zeroes, followed by all ones.

//For example,

//Input: { 1, 0, 1, 0, 1, 0, 0, 1 }

//Output: { 0, 0, 0, 0, 1, 1, 1, 1 }


import java.util.Scanner;

public class day1_Nikunj {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[] arr = new int[n];
		for(int i=0;i<n;i++) {
			arr[i] =sc.nextInt();
		}
		
		System.out.println(Arrays.toString(sort(arr,n)));
	}

	private static int[] sort(int[] arr,int n) {
		int count=0;
		for(int i=0;i<n;i++) {
			if(arr[i]==0) count++;
		}
		for(int i=0;i<count;i++) arr[i]=0;
		for(int i=count;i<n;i++) arr[i]=1;
		
		return arr;
	}

}
