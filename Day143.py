class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        max_sum = float('-inf')

        left_sum = sum(A[:B])
        max_sum = max(max_sum, left_sum)
        window_sum = left_sum
        for i in range(B):
            window_sum -= A[B - 1 - i]
            window_sum += A[n - 1 - i]
            max_sum = max(max_sum, window_sum)
        
        return max_sum
