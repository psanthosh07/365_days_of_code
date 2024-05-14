class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        count=0
        count = 1 
        max_so_far = A[0]  
        for i in range(1, len(A)):
            if A[i] > max_so_far:
                count += 1
                max_so_far = A[i]
    
        return count
