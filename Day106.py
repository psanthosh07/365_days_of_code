class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        B=str(A)
        pr=1
        for i in B:
            pr*=int(i)
        return pr 
        
