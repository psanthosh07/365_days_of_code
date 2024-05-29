class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def reverseList(self, A):
        if A is None or A.next is None:
            return A
        
        # Recursively reverse the rest of the list
        new_head = self.reverseList(A.next)
        
        # Connect current node to the reversed list
        A.next.next = A
        A.next = None
        
        return new_head
def printList(head):
    while head:
        print(head.val, end=" -> " if head.next else "")
        head = head.next
    print()
