"""
## Q.10) Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

 

Example 1:

- Input: s = "bcabc"
- Output: "abc"

Example 2:

- Input: s = "cbacdcbc"
- Output: "acdb"

"""


class Solution:
    def __init__(self, str):
        self.str = str
        self.len = len(str)
        self.dict = {}
        self.stack = []

    def smallestSubsequence(self):
        for i in range(self.len):
            self.dict[self.str[i]] = i
        for i in range(self.len):
            if self.str[i] in self.stack:
                continue
            while self.stack and self.str[i] < self.stack[-1] and self.dict[self.stack[-1]] > i:
                self.stack.pop()
            self.stack.append(self.str[i])
        return "".join(self.stack)


if __name__ == "__main__":
    str = input("Enter String: ")
    obj = Solution(str)
    print(obj.smallestSubsequence())
