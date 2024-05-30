class Solution:
    # @param A : integer
    # @return a string
    def findDigitsInBinary(self, A):
        if A == 0:
            return "0"
        
        binary_representation = ""
        while A > 0:
            remainder = A % 2
            binary_representation = str(remainder) + binary_representation
            A = A // 2
        
        return binary_representation
