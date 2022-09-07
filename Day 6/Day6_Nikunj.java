// ## Q6) Alice is rearranging her library. She takes the innermost shelf and reverses the order of books. She breaks the walls of the shelf. In the end, there will be only books and no shelf walls. Print the order of books.
// Opening and closing walls of shelves are shown by '/' and '\' respectively whereas books are represented by lower case alphabets.

// - Input format:
// The first line contains string _s_ displaying her library.

// - Output format:
// Print only one string displaying Alice's library after rearrangement.

// Constraints: 2≤|s|≤10^3

// Note:
// The first character of the string is '/' and the last character of the string is '\' indicating outermost walls of the shelf. 

// - Sample Input:  /u/love\i\
// - Sample Output: iloveu


import java.util.Scanner;
import java.util.Stack;

public class day6_Nikunj {

		public static String reverse(String s) {
			String x = "";
			for (int i = s.length() - 1; i > -1; i--) {
				x += s.charAt(i);
			}
			return x;
		}

		public static void main(String args[]) throws Exception {

			Scanner sc = new Scanner(System.in);
			String s = sc.nextLine();
			Stack<String> stack = new Stack<>();

			String x = "";

			for (int i = 0; i < s.length(); i++) {
				if (s.charAt(i) == '/') {
					stack.push(x);
					x = "";
				}
				else if (s.charAt(i) == '\\') {
					String rev = reverse(x);
					String temp = "";
					if (!stack.empty()) {
						temp = stack.pop() + rev;
					} else {
						temp = rev;
					}
					x = temp;
				} else {
					x += s.charAt(i);
				}
			}
			System.out.println(x);
		}
}
