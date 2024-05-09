class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        reciprocal_count = {}

        for i in range(len(A)):
            if A[A[i] - 1] == i + 1 and A[i] != i + 1:
                reciprocal_count[(min(i + 1, A[i]), max(i + 1, A[i]))] = 1
        total_gifts = sum(count for count in reciprocal_count.values())
        
        return total_gifts
