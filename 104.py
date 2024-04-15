class Solution:
    # @param A : integer
    # @return a strings
    def solve(self, A):
        if A>=3 and A<=5:
            return "Spring"
        elif A>=5 and A<=8:
            return "Summer"
        elif A>=8 and A<=11:
            return "Autumn"
        elif A in [12,1,2]:
            return "Winter"
        else:
            return "Invalid"
