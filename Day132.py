class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        non_empty_packets = [packet for packet in A if packet != 0]
        empty_packets_count = len(A) - len(non_empty_packets)
        return non_empty_packets + [0] * empty_packets_count
