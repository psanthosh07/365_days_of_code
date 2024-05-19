class Solution:
    # @param A : string
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        max_count = 0
        n = len(A)
        for i in range(0, n, B):
            substring = A[i:i+B]  
            count_a = substring.count('a') 
            max_count = max(max_count, count_a) 
        
        return max_count
