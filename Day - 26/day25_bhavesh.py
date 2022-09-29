V_SUM_MAX = 1000
N_MAX = 100
W_MAX = 10000000
 

dp = [[ 0 for i in range(N_MAX)]
          for i in range(V_SUM_MAX + 1)]
v = [[ 0 for i in range(N_MAX)]
         for i in range(V_SUM_MAX + 1)]
 

def solveDp(r, i, w, val, n):
     
    
    if (r <= 0):
        return 0
    if (i == n):
        return W_MAX
    if (v[r][i]):
        return dp[r][i]
 
    
    v[r][i] = 1
 
    
    dp[r][i] = min(solveDp(r, i + 1, w, val, n),
            w[i] + solveDp(r - val[i], i + 1,
                            w, val, n))
    return dp[r][i]
 

def maxWeight( w, val, n, c):
 
    
    
   
    for i in range(V_SUM_MAX, -1, -1):
        if (solveDp(i, 0, w, val, n) <= c):
            return i
 
    return 0
 

if __name__ == '__main__':
    w = [1, 2, 3, 4]
    val = [3, 4, 5, 7]
    n = len(w)
    C = 5
 
    print(maxWeight(w, val, n, C))
