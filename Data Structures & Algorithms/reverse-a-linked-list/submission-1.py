# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # If linked list is empty or having only one element, then return the same
        if not (head and head.next):
            return head

        # I am going to maintain two pointers, one is the head and the other one
        # the next node which are going to be incremented one by one
        next_node = head.next

        # The first node will have pointing to nothing in the reversed linked list
        head.next = None

        # Loop while there is a valid node
        while next_node:
            next_next_node = next_node.next
            next_node.next = head
            head = next_node
            next_node = next_next_node

        return head
             

        