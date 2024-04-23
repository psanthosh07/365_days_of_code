# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def swapPairs(self, A):

        if not A or not A.next:
            return A
        prev = ListNode(0)  
        prev.next = A
        current = prev

        while current.next and current.next.next:

            first_node = current.next
            second_node = current.next.next

            first_node.next = second_node.next
            second_node.next = first_node
            current.next = second_node

            current = current.next.next

        return prev.next
