#matrix
M = 3
N = 3


      def searchMatrix (matrix, K):
    low = 0
    high = M-1
    while (low <= high):
      mid = low + int((high - low)/2)
      
      if (K >= matrix[mid][0] and
          K <= matrix[mid][N-1]):
     
      
      if  (K < matrix[mid][0]:
           high = mid - 1
           else: 
           low = mid + 1
           
           return False 
           
           if __name__ == '__main__':
    matrix = [1, 2, 3
             4, 5, 6
             7, 8, 9]
    K = 3
    if (searchMatrix(matrix, K)):
        print("Found")
    else:
        print("Not found")
           
