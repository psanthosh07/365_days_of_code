class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        class TrieNode:
            def __init__(self):
                self.children = {}
                
        class Trie:
            def __init__(self):
                self.root = TrieNode()
                
            def insert(self, num):
                node = self.root
                for i in range(31, -1, -1):
                    bit = (num >> i) & 1
                    if bit not in node.children:
                        node.children[bit] = TrieNode()
                    node = node.children[bit]
                    
            def search(self, num):
                node = self.root
                xor_value = 0
                for i in range(31, -1, -1):
                    bit = (num >> i) & 1
                    if 1 - bit in node.children:
                        xor_value |= (1 << i)
                        node = node.children[1 - bit]
                    else:
                        node = node.children[bit]
                return xor_value

        trie = Trie()
        for num in B:
            trie.insert(num)
        max_xor = 0
        for num in A:
            max_xor = max(max_xor, trie.search(num))
        return max_xor
