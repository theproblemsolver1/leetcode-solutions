# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Create dummy node
        dummy = ListNode(0)
        dummy.next = head
        
        # Previous pointer
        prev = dummy

        # Traverse list
        while prev.next and prev.next.next:
            
            first = prev.next
            second = prev.next.next

            # Swap
            first.next = second.next
            second.next = first
            prev.next = second

            # Move pointer
            prev = first

        return dummy.next