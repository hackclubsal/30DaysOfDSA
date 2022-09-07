//#Q4) Given a positive integer num, write a function that returns true if num is a perfect square else false.

//Note: Do not use the in-built methods to calculate square root or power.

//Example-1:

//Input: isPerfectSquare(25)'
//Output: true
//Example-2:

//Input: isPerfectSquare(30)
//Output:false
//The time complexity of the method should be O(log n).

public class day4_Nikunj {

	public static void main(String[] args) {
		
		int num=26;
		System.out.println(perfectSQ(num));

	}

	private static boolean perfectSQ(int num) {
		
		int l=0;
		int r=num;
		while(l<=r) {
			int mid = (l+r)/2;
			if(mid*mid==num) return true;
			else if(mid*mid<num) l=mid+1;
			else r=mid-1;
		}
		
		return false;
	}

}
