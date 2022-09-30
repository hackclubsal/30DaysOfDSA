/*Q.16) Given a set of n integers denoting the strength of each student participating in a tug of war, divide the students into 2 equal parts such that the difference between the strengths of both the groups is minimum. Return the difference between the strengths of both the groups.
Note: If the number of students is odd, one group will have an extra student.

Examples-1:

Input:
strengths: [1, 2, 3, 4]

group 1: [1, 4] ,group 2: [2, 3]

Output: difference: 0
Example-2:

Input:
strengths: [1, 2, 3, 4, 5]

group 1: [1, 2, 5], group 2: [3, 4]

Output: difference: 1*/

import java.util.ArrayList;

public class Day16Kaushik {   

	public static void main(String args[]) {
		int[] nums = {1,2,3,4,5};
		minimum_diffrence(nums,0, new ArrayList<Integer>(),new ArrayList<Integer>(),0,0);
		System.out.println("arrays :"+ans);
		System.out.println("diffrence between them :"+mindiff);
	}

	static int mindiff = Integer.MAX_VALUE;
	static String ans="";
	
	public static void minimum_diffrence(int[] nums,int vidx,ArrayList<Integer> set1,ArrayList<Integer> set2,int soset1,int soset2) {
		
		if(vidx==nums.length) {
			int delta = Math.abs(soset1-soset2);
			
			if(delta<mindiff) {
				mindiff=delta;
				ans = set1+" "+set2;
			}
			return;
		}
		
		if(set1.size()<(nums.length+1)/2) {
			set1.add(nums[vidx]);
			minimum_diffrence(nums, vidx+1, set1, set2, soset1 + nums[vidx], soset2);
			set1.remove(set1.size()-1);
		}
		
		if(set2.size()<(nums.length+1)/2) {
			set2.add(nums[vidx]);
			minimum_diffrence(nums, vidx+1, set1, set2, soset1, soset2 + nums[vidx]);
			set2.remove(set2.size()-1);
		}
		 
		
	}
	
}