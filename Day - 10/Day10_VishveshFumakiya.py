#Day10 remove duplicate and result in lexicographical order
def removeDup(s):
	cur = [0] * 26
	vis = [0] * 26
	n = len(s)
	for i in s:
		cur[ord(i) - ord('a')] += 1

	fin = []
	for i in range(n):
		cur[ord(s[i]) - ord('a')] -= 1
		if(not vis[ord(s[i]) - ord('a')]):
			while (len(fin) > 0 and fin[-1] > s[i] and cur[ord(fin[-1]) - ord('a')] > 0):
				vis[ord(fin[-1]) - ord('a')] = 0
				del fin[-1]

		fin += s[i]
		vis[ord(s[i]) - ord('a')] = 1
	return "".join(fin)

S = "bcabc"
res = removeDup(S)
print(res)
