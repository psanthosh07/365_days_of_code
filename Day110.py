class Solution:
    # @param A : string
    # @return a list of integers
    def solve(self, A):
        alp="abcdefghijklmnopqrstuvwxyz"
        count={}
        for i in alp:
            count[i]=0
        for i in A:
            count[i]+=1
        return count.values()
