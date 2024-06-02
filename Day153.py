class Solution:
	# @param A : tuple of integers
	# @param B : integer
	# @return an integer
	def findCount(self, A, B):
        
        def find_first_occurrence(A, B):
            left, right = 0, len(A) - 1
            first_occurrence = -1
            while left <= right:
                mid = (left + right) // 2
                if A[mid] == B:
                    first_occurrence = mid
                    right = mid - 1 
                elif A[mid] < B:
                    left = mid + 1
                else:
                    right = mid - 1
            return first_occurrence

        def find_last_occurrence(A, B):
            left, right = 0, len(A) - 1
            last_occurrence = -1
            while left <= right:
                mid = (left + right) // 2
                if A[mid] == B:
                    last_occurrence = mid
                    left = mid + 1 
                elif A[mid] < B:
                    left = mid + 1
                else:
                    right = mid - 1
            return last_occurrence

        first_occurrence = find_first_occurrence(A, B)
        if first_occurrence == -1:
            return 0
        last_occurrence = find_last_occurrence(A, B)
        return last_occurrence - first_occurrence + 1
