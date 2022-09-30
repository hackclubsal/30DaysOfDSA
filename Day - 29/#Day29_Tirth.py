def ispalindrome(s):

	l = len(s)
	
	i = 0
	j = l - 1
	while i <= j:
	
		if(s[i] != s[j]):
			return False
		i += 1
		j -= 1
	
	return True

if __name__ == "__main__":
	
	s = "baaba"
	cnt = 0
	flag = 0
	
	while(len(s) > 0):
	
		if(ispalindrome(s)):
			flag = 1
			break
		
		else:
			cnt += 1
		
			s = s[:-1]
	
	if(flag):
		print(cnt)
