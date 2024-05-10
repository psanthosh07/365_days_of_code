class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        x_you, y_you = min(A, key=lambda point: (point[0], point[1]))
        x_friend, y_friend = min(A, key=lambda point: (point[1], point[0]))
        distance = abs(x_you - x_friend) + abs(y_you - y_friend)

        return distance
