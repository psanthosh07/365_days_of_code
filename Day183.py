class Solution:
    # @param A : integer
    # @return an integer
    def colorful(self, A):
        str_A = str(A)
        products = set()

        n = len(str_A)

        for length in range(1, n + 1):  
            for start in range(n - length + 1):  
                subsequence = str_A[start:start + length]
                product = 1
                for char in subsequence:
                    product *= int(char)

                if product in products:
                    return 0
                products.add(product)

        return 1
