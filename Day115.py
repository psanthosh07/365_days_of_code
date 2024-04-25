class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        if not A:
            return 0

        max_num = A[0]
        min_num = A[0]
        

        for num in A[1:]:

            if num > max_num:
                max_num = num
            elif num < min_num:
                min_num = num
        return max_num + min_num
