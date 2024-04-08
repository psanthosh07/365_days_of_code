class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):

        char_count = {}
        for char in A:
            char_count[char] = char_count.get(char, 0) + 1
        odd_count = 0
        for count in char_count.values():
            if count % 2 != 0:
                odd_count += 1

        if len(A) % 2 == 0:
            return 0 if odd_count > 0 else 1
        else:
            return 1 if odd_count == 1 else 0
        
