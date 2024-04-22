class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def permuteStrings(self, A, B):
        if len(A) != len(B):
            return 0
        
        count = [0] * 26 

        for char in A:
            count[ord(char) - ord('a')] += 1

        for char in B:
            count[ord(char) - ord('a')] -= 1

        for c in count:
            if c != 0:
                return 0
        
        return 1
