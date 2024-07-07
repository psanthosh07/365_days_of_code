class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        from collections import Counter

        count_A = Counter(A)
        
        result = []

        for element in B:
            if count_A[element] > 0:
                result.append(element)
                count_A[element] -= 1
        
        return result
