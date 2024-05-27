class Solution:
	# @param x : integer
	# @return an integer
	def reverse(self, x):
        negative = x < 0

        reversed_str = str(abs(x))[::-1]
        reversed_num = int(reversed_str)

        if negative:
            reversed_num *= -1

        if reversed_num < -2**31 or reversed_num > 2**31 - 1:
            return 0
        
        return reversed_num
