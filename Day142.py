class Solution:
    # @param A : string
     # @return an long
    def solve(self, A):
        total = 0
        current_number = 0
        for char in A:
            if char.isdigit():
                current_number = current_number * 10 + int(char)
            else:
                total += current_number
                current_number = 0
        total += current_number  
        return total
