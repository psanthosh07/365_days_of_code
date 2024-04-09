class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        if (A % 4 == 0 and A % 100 != 0) or (A % 400 == 0):
            return 1  
        else:
            return 0 
