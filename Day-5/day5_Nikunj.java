//Given a sorted list of numbers in which all elements appear twice except one element that appears only once, find the number that appears only once.
//Example: 1, 1, 2, 3, 3, 4, 4 Here, ‘2’ appears once and all other elements appear twice.

//Input: ([1, 1, 2, 3, 3, 4, 4])
//=>it’s 2
//Output:2
//Expected Time Complexity: O(log n)

public class day5_Nikunj {

	public static void main(String[] args) {
		int[] arr = {1, 1, 2,2, 4, 5, 5, 6, 6};
		int ans = not_appears_twice(arr);
		System.out.println(ans);
	}

	private static int not_appears_twice(int[] arr) {
		int l=0, r=arr.length-1;
		while(l<=r) {
			int mid = l+(r-l)/2;
			
			if(arr[mid]!=arr[mid-1] && arr[mid]!=arr[mid+1])
				return arr[mid];
			else if((arr[mid] == arr[mid + 1] && mid % 2 == 0) || (arr[mid] == arr[mid - 1] && mid % 2 != 0))
				l=mid+1;
			else 
				r=mid-1;
		}
		return -1;
	}

}
