class Solution:
    # @param x : integer
    # @param n : integer
    # @param d : integer
    # @return an integer
    def pow(self, x, n, d):
        if n == 0:
            return 1 % d

        result = 1
        base = x % d
        while n > 0:
            if n % 2 == 1:
                result = (result * base) % d
            n //= 2
            base = (base * base) % d

        return result
