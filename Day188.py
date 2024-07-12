class Solution:
    def isPalindrome(self, x: int) -> bool:
        l=str(x)
        if l[::-1]==l:
            return True
        return False
