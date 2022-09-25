package The_30daydsa;
import java.util.ArrayList;
import java.util.HashMap;

//Q.12) Given an array of integers and a number K. Find the count of distinct elements in every window of size K in the array.
//Example 1:

//Input: N = 7, K = 4 A[] = {1,2,1,3,4,2,3}
//Output: 3 4 4 3
//Explanation:

//Window 1 of size k = 4 is 1 2 1 3. Number of distinct elements in this window are 3. Window 2 of size k = 4 is 2 1 3 4. Number of distinct elements in this window are 4. Window 3 of size k = 4 is 1 3 4 2. Number of distinct elements in this window are 4. Window 4 of size k = 4 is 3 4 2 3. Number of distinct elements in this window are 3.

//Example 2:

//Input: N = 3, K = 2* A[] = {4,1,1}
//Output: 2 1


public class day12_Nikunj {

	public static void main(String[] args) {
		int[] a = {1,2,1,3,4,2,3};
		int k=4;
		ArrayList<Integer> ans = countDistinct(a, a.length,k);
		System.out.println(ans);
	}
	
	 static ArrayList<Integer> countDistinct(int A[], int n, int k)
	    {
	         ArrayList<Integer> l=new ArrayList<>();
	        HashMap<Integer,Integer> map=new HashMap<>();
	        int j=0;
	        for(int i=0;i<n;i++){
	            map.put(A[i],map.getOrDefault(A[i],0)+1);
	            if(i-j+1==k){
	                l.add(map.size());
	                if(map.get(A[j])==1){
	                    map.remove(A[j]);
	                }else{
	                    map.put(A[j],map.get(A[j])-1);
	                }
	                j++;
	            }
	        }
	        return l;
	    }
}
