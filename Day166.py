class Solution:
    # @param A : list of integers
    # @return a strings
    def solve(self, A):
        mean=sum(A)/len(A)
        sum_squares = sum((x - mean) ** 2 for x in A)
        variance = sum_squares / len(A)
    
        return round(variance, 2)
            
