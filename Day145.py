class Solution:
	# @param A : integer
	# @return an integer
	def isPalindrome(self, A):
		b=str(A)
		if b==b[::-1]:
			return 1
		else:
			return 0
