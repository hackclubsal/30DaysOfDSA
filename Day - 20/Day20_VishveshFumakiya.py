#Day 20 -  length of the longest increasing path
class Solution(object):
    def solve(self,i,j,matrix):
        if self.dp[i][j]:
            return self.dp[i][j]
        self.dp[i][j] = 1
        temp = 0
        for r in range(i-1,i+2):
            for c in range(j-1,j+2):
                if r==i and c==j or (abs(r-i)==1 and abs(c-j)==1):
                    continue
                if c>=0 and r>=0 and r<len(matrix) and c<len(matrix[0]) and matrix[r][c]>matrix[i][j]:
                    temp = max(temp,self.solve(r,c,matrix))
                self.dp[i][j]+=temp
                return self.dp[i][j]
    def longestIncreasingPath(self, matrix):
        if not matrix:
            return 0
        self.dp = [ [0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        self.ans = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if self.dp[i][j]==0:
                    self.solve(i,j,matrix)
                    self.ans = max(self.ans,self.dp[i][j])
        return self.ans

ob = Solution()
matrix = [[9,9,4],[6,6,8],[2,1,1]]
print(ob.longestIncreasingPath(matrix))
