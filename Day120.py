class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        count = 0
        while A:
            count += A & 1
            A >>= 1
        return count
