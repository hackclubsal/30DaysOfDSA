import math as mt
 

 
 
def countWindowDistinct(win, K):
 
    dist_count = 0
 
    
    for i in range(K):
 
        
        
        j = 0
        while j < i:
            if (win[i] == win[j]):
                break
            else:
                j += 1
        if (j == i):
            dist_count += 1
 
    return dist_count
 
 


def countDistinct(arr, N, K):
 
    
    for i in range(N - K + 1):
        print(countWindowDistinct(arr[i:K + i], K))
 
 

if __name__=='__main__':
  arr = [1, 2, 1, 3, 4, 2, 3]
  K = 4
  N = len(arr)
   
  
  countDistinct(arr, N, K)
