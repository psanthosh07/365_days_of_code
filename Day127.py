class Solution:
	# @param A : string
	# @return an integer
	def titleToNumber(self, A):
        column_number = 0
        for char in A:
            column_number = column_number * 26 + (ord(char) - ord('A') + 1)
        return column_number
