class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        l=[]
        p=0
        n=0
        for i in A:
            if i>0:
                p+=1
            elif i<0:
                n+=1
        l=[p,n]
        return l
