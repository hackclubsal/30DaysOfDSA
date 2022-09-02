package The_30daydsa;

import java.util.Arrays;

//Given an array, rotate the array to the right by k steps, where k is non-negative.
//For Example,

//Input: nums = [1,2,3,4,5,6,7] , k = 3

//Output: [5,6,7,1,2,3,4]

//Explanation:

//rotate 1 steps to the right: [7,1,2,3,4,5,6]
//rotate 2 steps to the right: [6,7,1,2,3,4,5]
//rotate 3 steps to the right: [5,6,7,1,2,3,4]

public class day2_Nikunj {

	public static void main(String[] args) {

		int[]arr = {5,6,7,8,9,10,11};
		int k=2;
		
		System.out.println(Arrays.toString(rotate(arr,k)));
	}

	private static int[] rotate(int[] arr, int k) {
		int[] temp = new int[k];
		int n= arr.length;
		for(int i=0;i<k;i++) {
			temp[i]=arr[n-k+i];
		}
		for(int i=n-1;i>=k;i--) {
			arr[i]=arr[i-k];
		}
		for(int i=0;i<k;i++) {
			arr[i]=temp[i];
		}
		return arr;
	}

}
