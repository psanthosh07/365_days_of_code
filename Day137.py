class Solution:
    # @param A : list of strings
    # @return an integer
    def solve(self, A):
        seen_letters = set()

        for word in A:
            for char in word:
                seen_letters.add(char)

        if len(seen_letters) == 26:
            return 1
        else:
            return 0  
