class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        count=0
        for i in A:
            if i<=B:
                count+=1
            else:
                continue
        return count
                
                
