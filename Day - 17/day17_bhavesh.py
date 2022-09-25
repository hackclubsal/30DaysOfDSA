import sys
 


def minimumChar(S1, S2):
     
    
    n, m = len(S1), len(S2)
 
    ans = sys.maxsize
 
    
    for i in range(m - n + 1):
        minRemovedChar = 0
 
        
        
        
        for j in range(n):
            if (S1[j] != S2[i + j]):
                minRemovedChar += 1
                 
        
        
        ans = min(minRemovedChar, ans)
         
    
    return ans
     

if __name__ == '__main__':
    S1 = "hello"
    S2 = "seldom"
    print(minimumChar(S1, S2))
