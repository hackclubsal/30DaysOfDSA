def checkStr(s2, s1):
	if s2 in s1:
		return s1.index(s2)
	return -1

s1 = "helloworld"
s2 = "low"
res = checkStr(s2,s1)
print(res)
