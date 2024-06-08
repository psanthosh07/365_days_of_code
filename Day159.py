class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def rotateArray(self, A, B):
        n = len(A)
        B = B % n  
        return A[B:] + A[:B]
