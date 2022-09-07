public class Day5 {

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
