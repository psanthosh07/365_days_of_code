class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        A_str = str(A)

        num_digits = len(A_str)

        armstrong_sum = 0

        for digit_char in A_str:
            digit = int(digit_char)
            armstrong_sum += digit ** num_digits

        if armstrong_sum == A:
            return 1
        else:
            return 0

