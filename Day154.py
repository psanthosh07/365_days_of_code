class Solution:
	# @param A : list of integers
	# @return an integer
	def bulbs(self, A):
        flips = 0
        current_state = 0  

        for bulb in A:

            if bulb == current_state:  
                flips += 1
                current_state = 1 - current_state

        return flips
