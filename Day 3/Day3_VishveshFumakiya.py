#Day3
def searchMatrix(matrix, K):
	low = 0
	high = M - 1
	while(low <= high):
		mid = low +  int((high - low) / 2)

		if(matrix[mid] == K):
			return True

		if(matrix[mid] < K):
			low = mid + 1
		else:
			high = mid -1
	return False

matrix = [1, 2, 3,
			4, 5, 6,
			7, 8, 9]
K = 10
M = len(matrix)
if(searchMatrix(matrix, K)):
	print("true")
else:
	print("false")
