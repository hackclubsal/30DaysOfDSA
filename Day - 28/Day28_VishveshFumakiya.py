import sys
def isPalindrome(X, i, j):
    while i <= j:
        if X[i] != X[j]:
            return False
        i = i + 1
        j = j - 1 
    return True

def findMinCuts(X, i, j):
    if i == j or isPalindrome(X, i, j):
        return 0
    min = sys.maxsize
    for k in range(i, j):
        count = 1 + findMinCuts(X, i, k) + findMinCuts(X, k + 1, j)
        if count < min:
            min = count
    return min

def findMinimumCuts(X):
    if not X:
        return 0
    return findMinCuts(X, 0, len(X) - 1)
 
X = 'aabc'
print('Min cuts :', findMinimumCuts(X)) 
