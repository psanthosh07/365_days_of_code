class Solution:
	# @param A : integer
	# @param B : integer
	# @param C : integer
	# @return an integer
	def Mod(self, A, B, C):
        if C == 0:
            return 0
        if B == 0:
            return 1 % C
        
        A = A % C
        result = 1
        
        while B > 0:
            if B % 2 == 1:  
                result = (result * A) % C
            A = (A * A) % C 
            B //= 2  
            
        return result
