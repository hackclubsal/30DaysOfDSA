import java.util.*;

class Day6_AkashRChandran {
  public static String reverse(String s) {
    String x = "";
    for (int i = s.length() - 1; i > -1; i--)
      x += s.charAt(i);
    return x;
  }

  public static void main(String args[]) throws Exception {
    Scanner sc = new Scanner(System.in);
    String s = sc.nextLine();
    Stack < String > stack = new Stack < > ();
    String x = "";
    for (int i = 0; i < s.length(); i++) {
      if (s.charAt(i) == '/') {
        stack.push(x);
        x = "";
      } else if (s.charAt(i) == '\\') {
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
	sc.close();
  }
}