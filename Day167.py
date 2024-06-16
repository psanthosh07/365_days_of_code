class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        count = 0
        while A > 0 and A & 1 == 0:
            count += 1
            A >>= 1
        return count
