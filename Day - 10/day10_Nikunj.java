import java.util.Map;
import java.util.Scanner;
import java.util.Stack;
import java.util.TreeMap;

//Q.10) Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

//Example 1:
//Input: s = "bcabc"
//Output: "abc"

//Example 2:
//Input: s = "cbacdcbc"
//Output: "acdb"

public class day10_Nikunj {

	public static void main(String[] args) {
		Map<Character,Boolean> map = new TreeMap<>();
		Scanner sc = new Scanner(System.in);
		String input = sc.next();
		
		for(int i=0;i<input.length();i++) {
			if(!map.containsKey(input.charAt(i)))
				map.put(input.charAt(i), true);
		}
		String ans=map.keySet().toString();
		System.out.println(ans);
		
//		required approch for output
		
		String ans2 = removeDuplicateLetters(input);
		System.out.println(ans2);
	}
	
	public static String removeDuplicateLetters(String s) {
        int freq[] = new int[26];
        boolean exists[] = new boolean[26];
        Stack<Character> st = new Stack<>();
        
        for(int i=0;i<s.length();i++)
            freq[s.charAt(i) - 'a']++;
        
        for(int i=0;i<s.length();i++)
        {
            char ch = s.charAt(i);
            freq[ch-'a']--;
            if(exists[ch-'a'] == true)
                continue;
            while(st.size()>0 && st.peek()>ch && freq[st.peek()-'a']>0 )
                exists[st.pop() - 'a'] = false;
            st.push(ch);
            exists[ch-'a'] = true;
        }
        
        StringBuilder str = new StringBuilder();
        
        while(st.size() > 0)
            str.append(st.pop());
        
        return str.reverse().toString();
    }

}
