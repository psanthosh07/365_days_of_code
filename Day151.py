class Solution:
    # @param A : string
    # @return an integer
    def isPalindrome(self, A):
        filtered_string = ''.join(char.lower() for char in A if char.isalnum())
        if filtered_string == filtered_string[::-1]:
            return 1
        else:
            return 0
