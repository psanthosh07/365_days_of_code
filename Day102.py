class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        count1=0
        count2=0
        for i in A:
            if i>C:
                count1+=1
        for i in B:
            if i<C:
                count2+=1
        return max(count1,count2)
