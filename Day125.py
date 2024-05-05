class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @return an integer
    def solve(self, A, B, C, D):

        if (A == B and C == D) or (A == C and B == D) or (A == D and B == C):
            return 1
        else:
            return 0
