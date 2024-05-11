class Solution:
    # @param A : integer
    # @param B : integer
     # @return an long
    def solve(self, A, B):
        current_element = A
        for _ in range(B - 1):
            if current_element % 2 == 0:
                current_element //= 2
            else:
                current_element = 3 * current_element + 1
        return current_element
