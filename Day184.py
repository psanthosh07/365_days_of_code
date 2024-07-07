class Solution:
    # @param matrix : tuple of list of integers
    # @return an integer
    def solve(self, matrix):
        n = len(matrix)
        if n == 0:
            return 0
        
        m = len(matrix[0])
        if m == 0:
            return 0

        seen_pairs = {}
        
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 1:
                    for k in range(j + 1, m):
                        if matrix[i][k] == 1:
                            if (j, k) in seen_pairs:
                                return 1
                            seen_pairs[(j, k)] = True
        
        return 0
