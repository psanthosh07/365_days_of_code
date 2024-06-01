import math
class Solution:
	# @param A : integer
	# @return a list of integers
	def allFactors(self, A):
        factors = set()
        for i in range(1, int(math.sqrt(A)) + 1):
            if A % i == 0: 
                factors.add(i)
                factors.add(A // i)

        return sorted(factors)
