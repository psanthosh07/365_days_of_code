class Solution:
    # @param A : list of list of integers
    # @return an integer
    def minPathSum(self, A):
        if not A:
            return 0

        rows = len(A)
        cols = len(A[0])
        dp = [[0] * cols for _ in range(rows)]

        dp[0][0] = A[0][0]
        for i in range(1, cols):
            dp[0][i] = dp[0][i - 1] + A[0][i]

        for i in range(1, rows):
            dp[i][0] = dp[i - 1][0] + A[i][0]
  
        for i in range(1, rows):
            for j in range(1, cols):
                dp[i][j] = A[i][j] + min(dp[i - 1][j], dp[i][j - 1])

        return dp[rows - 1][cols - 1]
