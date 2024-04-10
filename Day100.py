class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        odd_count = sum(1 for num in A if num % 2 != 0)
        if odd_count == 0:
            return 0
        else:
            return pow(2, odd_count, 10**9 + 7) - 1
