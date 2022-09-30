class Day10 {
    public String removeDuplicateLetters(String s) {
        int[] last = new int[26];
        boolean[] seen = new boolean[26];

        // Last occurrance 
        int index = 0;
        for(char current : s.toCharArray()) {
            last[current - 'a'] = index;
            index++;
        }

        ArrayDeque<Integer> stack = new ArrayDeque<>();
        StringBuilder sb = new StringBuilder();
        int currIndex;

        index = -1;
        for(char current : s.toCharArray()) {
            currIndex = current - 'a';
            index++;
            if(seen[currIndex]) { continue; }
            while(!stack.isEmpty() && currIndex < stack.peek() && last[stack.peek()] > index) {
                seen[stack.pop()] = false;

            }
            stack.push(currIndex);
            seen[currIndex] = true;

        }

        while(!stack.isEmpty()) {
            sb.insert(0,(char)(stack.pop() + 'a'));
        }

        return sb.toString();
    }
}
