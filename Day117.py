class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        num_set = set()  
        
        for num in A:

            if num - B in num_set or num + B in num_set:
                return 1  
            num_set.add(num)  
            
        return 0  
