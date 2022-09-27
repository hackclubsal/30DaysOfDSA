def findCount(A, k):
	lis = []
	for i in range(len(A) - (k - 1)):
		lis.append(set(A[i:i+k]))
	for i in range(len(lis)):
		print(len(set(lis[i])), end = " ")

A = [1,2,1,3,4,2,3]
k = 4
findCount(A, k)
