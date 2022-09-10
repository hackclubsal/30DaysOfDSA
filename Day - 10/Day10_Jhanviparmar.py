def rdl(s):
	cnt = [0] * 26
	vis = [0] * 26
	n = len(s)
	for i in s:
		cnt[ord(i) - ord('a')] += 1
	res = []
	for i in range(n):
		cnt[ord(s[i]) - ord('a')] -= 1
		if (not vis[ord(s[i]) - ord('a')]):
			while (len(res) > 0 and
					res[-1] > s[i] and
		cnt[ord(res[-1]) - ord('a')] > 0):
				vis[ord(res[-1]) - ord('a')] = 0
				del res[-1]
			res += s[i]
			vis[ord(s[i]) - ord('a')] = 1
	return "".join(res)
if __name__ == '__main__':
	S = "bcabc"
	print(rdl(S))
