class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        total_fine = 0
    

        is_odd_day = B % 2 == 1
    
        for number in A:
            last_digit = number % 10
            if (is_odd_day and last_digit % 2 == 0) or (not is_odd_day and last_digit % 2 == 1):
                total_fine += C
    
        return total_fine
