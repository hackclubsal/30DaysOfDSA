#Day_8 Kadane's Algo
def maxSumSubArray(n):
	maxSum = 0
	curSum = 0
	for i in range(0, len(n)):
		curSum = curSum + n[i]
		if(curSum > maxSum):
			maxSum = curSum
		if(curSum < 0):
			curSum = 0
	return maxSum

N = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
res = maxSumSubArray(N)
print(res)
