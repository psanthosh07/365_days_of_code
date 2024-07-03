class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
            MOD = 10**9 + 7
            vowels = set('aeiou')
            vowel_count = 0
            consonant_count = 0
            result = 0
            
            for char in A:
                if char in vowels:
                    result = (result + consonant_count) % MOD
                    vowel_count += 1
                else:
                    result = (result + vowel_count) % MOD
                    consonant_count += 1
            
            return result
    
