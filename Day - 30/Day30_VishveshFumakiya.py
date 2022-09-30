def matPrint(arr):
         N = len(arr)
         for i in range (N):
                 for j in range (N):
                        print(str(arr[i][j]), end = " ")
                 print()

def matTranspose(arr):
         N = len(arr)
         for i in range(N):
                for j in range(i,N):
                        arr[i][j], arr[j][i] = arr[j][i],arr[i][j]

def colReverse(arr):
      N = len(arr)
      for i in range (N):
         k = N - 1
         for j in range(0,k):
                 arr[j][i], arr[k][i] = arr[k][i], arr[j][i]
                 k = k - 1

mat = [[1,2,3], [4,5,6], [7,8,9],];
matTranspose(mat)
colReverse(mat)
matPrint(mat)
