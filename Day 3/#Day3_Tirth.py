a = [1,2,3,4,5,6,7,8,9]
def checkKey(a,n):
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] == n:
                return True
A = [[1, 2, 3],
    [4, 5, 6],
	[7, 8, 9]]

n = int(input("What Is The Key?:"))

if checkKey(A,n):
    print("KEY IS IN THE MATRIX.")
else:
    print("KEY DOES NOT EXIST IN MATRIX.")
