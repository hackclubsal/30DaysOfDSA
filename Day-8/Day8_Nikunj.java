//Q8) Given an integer array N, find the contiguous subarray which has the largest sum and return its sum.
//Example-1:

//Input: N = [-2,1,-3,4,-1,2,1,-5,4]
//Output: 6
//Example-2:

//Input: N= [5,4,-1,7,8]
//Output: 23
//Time complexity must be O(n)

public class day8_Nikunj {

	public static void main(String[] args) {
		int[] arr = {-2,1,-3,4,-1,2,1,-5,4};
		long ans = maxSubarraySum(arr, 9);
		System.out.println(ans);
	}

	public static long maxSubarraySum(int[] arr, int n) {
		long cursum=0;
		long maxsum=0;
		
		for(int i=0;i<n;i++) {
			cursum+=arr[i];
			if(cursum>=maxsum) {
				maxsum=cursum;
			}
			if(cursum<0) {
				cursum=0;
				continue;
			}
		}
		return maxsum;
	}
}
