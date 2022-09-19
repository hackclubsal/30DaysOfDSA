import java.util.Scanner;

public class Day10_AKashRChandran {

	public static String removeDuplicates(String str1) {
		int[] ctr = new int[26];
		boolean[] in_stack = new boolean[26];
		char[] st_char = new char[str1.length()];
		int len = 0;

		for (char c : str1.toCharArray()) {
			ctr[c - 'a']++;
		}

		for (char c : str1.toCharArray()) {
			ctr[c - 'a']--;

			if (!in_stack[c - 'a']) {
				while (len > 0 && c < st_char[len - 1] && ctr[st_char[len - 1] - 'a'] > 0) {
					in_stack[st_char[--len] - 'a'] = false;
				}
				st_char[len++] = c;
				in_stack[c - 'a'] = true;
			}
		}
		return new String(st_char, 0, len);
	}

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		System.out.print("Enter the string: ");
		String letters = scan.nextLine();
		System.out.println("After removing duplicates: " + removeDuplicates(letters));
		scan.close();
	}
}