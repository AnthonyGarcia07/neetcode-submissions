# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            nxt = curr.next  # Save where we're going next
            curr.next = prev # Reverse the arrow
            prev = curr # Move prev forward
            curr = nxt # Move curr forward
        return prev
        