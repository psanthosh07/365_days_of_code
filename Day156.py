class Solution:
    # @param A : integer
    # @return a list of integers
    def primesum(self, A):

        def sieve(n):
            is_prime = [True] * (n + 1)
            p = 2
            while p * p <= n:
                if is_prime[p]:
                    for i in range(p * p, n + 1, p):
                        is_prime[i] = False
                p += 1
            primes = []
            for p in range(2, n + 1):
                if is_prime[p]:
                    primes.append(p)
            return primes

        primes = sieve(A)

        prime_set = set(primes)
        for prime in primes:
            if (A - prime) in prime_set:
                return [prime, A - prime]

