class Solution:
    # @param A : integer
    # @param B : integer
     # @return an long
    def solve(self, A, B):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        return (A * B) // gcd(A, B)

