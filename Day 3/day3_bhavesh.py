M = 3
N = 4
 

def binarySearch1D(arr, K):
    low = 0
    high = N - 1
    while (low <= high):
        mid = low + int((high - low) / 2)
 
        # if element found return true
        if (arr[mid] == K):
            return True
 
        
        if (arr[mid] < K):
            low = mid + 1
        else:
            high = mid - 1
 
   
    return False
 

def searchMatrix(matrix, K):
    low = 0
    high = M - 1
    while (low <= high):
        mid = low + int((high - low) / 2)
 
       
        if (K >= matrix[mid][0] and
            K <= matrix[mid][N - 1]):
            return binarySearch1D(matrix[mid], K)
 
        
        if (K < matrix[mid][0]):
            high = mid - 1
        else:
            low = mid + 1
 
    
    return False
 

if __name__ == '__main__':
    matrix = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]]
    K = 3
    if (searchMatrix(matrix, K)):
        print("True")
    else:
        print("False")
 
