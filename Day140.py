class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):

        if len(A) < 8 or len(A) > 15:
            return 0

        has_digit = False
        has_lower = False
        has_upper = False
        has_special = False

        special_characters = {'@', '#', '%', '&', '!', '$', '*'}
 
        for char in A:
            if char.isdigit():
                has_digit = True
            elif char.islower():
                has_lower = True
            elif char.isupper():
                has_upper = True
            elif char in special_characters:
                has_special = True
        if has_digit and has_lower and has_upper and has_special:
            return 1
        else:
            return 0
