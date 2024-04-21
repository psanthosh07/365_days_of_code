class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        def backtrack(start, size, xor_value):
            if size == 4:
                max_xor[0] = max(max_xor[0], xor_value)
                return
            for i in range(start, len(A)):
                backtrack(i + 1, size + 1, xor_value ^ A[i])

        max_xor = [float('-inf')]
        backtrack(0, 0, 0)
        return max_xor[0]
        
