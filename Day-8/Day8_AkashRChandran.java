
public class Day8_AkashRChandran {
	static int maxSumSubArray(int[] a) {
		int maximum_sum = 0;
		int current_sum = 0;
		for (int i = 0; i < a.length; i++) {
			current_sum = current_sum + a[i];
			if (current_sum > maximum_sum) {
				maximum_sum = current_sum;
			}
			if (current_sum < 0) {
				current_sum = 0;
			}
		}
		return maximum_sum;
	}
	public static void main(String[] args) {
		int [] a = {5,4,-1,7,8};
        System.out.println("Maximum contiguous sum is " + maxSumSubArray(a));
	}
}
