class Checkorder:
	def solve(self, s):
		n = len(s)
		def helper(pos, prev):
			if pos == n:
				return True
			num = len(str(prev))
			for i in range(num - 1, num + 1):
				if(s[pos:pos+i] and int(s[pos:pos+i]) == prev - 1):
					if(helper(pos + i, prev - 1)):
						return True
			return False
		for i in range(1, n//2 + 1):
			number = int(s[:i])
			if(helper(i, number)):
				return True
		return False		

res = Checkorder()
s = "10099989796"
print("Answer :", res.solve(s)) 
