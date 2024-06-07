class Solution:
	# @param A : list of integers
	# @return a list of integers
	def nextGreater(self, A):
        n = len(A)
        G = [-1] * n  
        stack = []
        
        for i in range(n):
           
            while stack and A[i] > A[stack[-1]]:
                index = stack.pop()
                G[index] = A[i]

            stack.append(i)
        
        return G
