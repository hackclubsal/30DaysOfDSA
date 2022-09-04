import java.util.Scanner;

public class Day4_AkashRChandran {
	public static boolean isPerfectSquare(int number) {
		int i = 1;
		while (number > 0) {
			number -= i;
			i += 2;
		}
		return number == 0;
	}

	public static void main(String args[]) {
		int m;
		Scanner scan = new Scanner(System.in);
		System.out.print("Enter the number: ");
		m = scan.nextInt();
		System.out.println("Number is a Perfect Square: " + isPerfectSquare(m));
		scan.close();
	}
}
