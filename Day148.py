class Solution:
	# @param A : integer
	# @return a list of integers
	def sieve(self, A):
        is_prime = [True] * (A + 1)
        is_prime[0] = is_prime[1] = False 
        p = 2
        while p * p <= A:
            if is_prime[p]:  
                for multiple in range(p * p, A + 1, p):
                    is_prime[multiple] = False
            p += 1
        primes = [num for num in range(2, A + 1) if is_prime[num]]
        return primes
