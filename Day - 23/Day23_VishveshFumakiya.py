def winMax(A, K):
    n = len(A)
    if n * K == 0:
        return []        
    return [max(A[i:i + K]) for i in range(n - K + 1)]

A = [1, -2, 3, 4, 5, 3, 4, -1]
K = 3
res = winMax(A, K)
print(res)
