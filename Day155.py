class Solution:
    # @param A : integer
    # @return a list of list of integers
    def prettyPrint(self, A):
        size = 2 * A - 1
        matrix = [[0] * size for _ in range(size)]
        
        for i in range(A):

            for j in range(i, size - i):
                matrix[i][j] = A - i
                matrix[size - i - 1][j] = A - i
                matrix[j][i] = A - i
                matrix[j][size - i - 1] = A - i
                
        return matrix
