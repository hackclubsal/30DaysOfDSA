import java.util.Scanner;

public class Day9_AkashRChandran {
	public static int compareVersion(String version1, String version2) {
		String[] v1s = version1.split("\\.");
		String[] v2s = version2.split("\\.");
		int i = 0;
		for (; i < v1s.length && i < v2s.length; i ++) {
			int v1 = Integer.parseInt(v1s[i]);
			int v2 = Integer.parseInt(v2s[i]);
			if (v1 > v2) {
				return 1;
			}
			if (v2 > v1) {
				return -1;
			}
		}
		if (i < v1s.length) {
			for (;i < v1s.length;i++) {
				if (Integer.parseInt(v1s[i]) != 0) {
					return 1;
				}
			}
		}
		if (i < v2s.length) {
			for (;i < v2s.length;i++) {
				if (Integer.parseInt(v2s[i]) != 0) {
					return -1;
				}
			}
		}
		return 0;
	}
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		System.out.print("Enter the version 1: ");
		String version1 = scan.nextLine();
		System.out.print("Enter the version 2: ");
		String version2 = scan.nextLine();
		int result = compareVersion(version1, version2);
		if (result == 1)
			System.out.print("version 2 < version 1");
		else if (result == -1)
			System.out.print("version 2 > version 1");
		else
			System.out.print("version 2 = version 1");
		scan.close();
	}
}