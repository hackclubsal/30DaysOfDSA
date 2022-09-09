package The_30daydsa;
import java.util.Scanner;

//Q9)Given two version numbers, compare them.
//A version number consists of one or more revisions connected by a dot. Each revisions consists of digits and may contain leading zeroes. Each revision consists atleast one digit.

//Revisions are 0-indexed from left to right. To compare two versions, compare revisions in the left-to-right order. Revisions are compared using their integer value ignoring any leading zeroes.

//Example 1:

//version 1: 1.1.0
//version 2: 1.2.0
//Output:
//version 2 > version 1.

//Example 2:

//version 1: 1.001.2
//version 2: 1.1.2
//Output:
//version 2 = version 1.

//Example 3:

//version 1: 1.100.2
//version 2: 1.1.2
//Output:
//version 2 < version 1.

public class day9_Nikunj {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String v1 = sc.next();
		String v2 = sc.next();
		
		String ans = check(v1,v2);
		System.out.println(ans);
	}

	private static String check(String v1, String v2) {
		
		String[] temp1 = v1.split("[.]",3);
		String[] temp2 = v2.split("[.]",3);
		
		for(int i=2;i>=0;i--) {
			int a = Integer.parseInt(temp1[i]);
			int b = Integer.parseInt(temp2[i]);
			
			if(a<b) {
				return "version 2 > version 1";
			}else if(a>b) {
				return "version 2 < version 1";
			}
		}
		return "version 2 = version 1";
	}

}
