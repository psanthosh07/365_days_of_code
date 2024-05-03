class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        A.sort(key=lambda x: x[1])
        
        end = A[0][1]
        count = 1
        for interval in A[1:]:
            start, current_end = interval
            if start > end:
                count += 1
                end = current_end
                
        return count
            
