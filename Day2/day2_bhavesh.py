#right rotation 

def RightRotate(a,n,k):
  
  k = k % n;
  
  for i in range(0,n):
    
    if(i<k):
      
      print(a[n+i-k], end= "");
      
      else:
        
        print(a[i-k], end="");
        
        print("\n");
        
        Array = [1,2,3,4,5,6,7];
        N = len(Array);
        K = 3;
        
        RightRotate(Array,N,K);
