# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # a. Use a dummy node pointing to head and set groupPrev = dummy
        dummy = ListNode(0, head)
        groupPrev = dummy
        
        while True:
            # b. Find the last node of the current group
            kth = self.getKth(groupPrev, k)
            if not kth:
                break  # Not enough nodes remaining, stop
                
            groupNext = kth.next  # Mark where the current group ends
            
            # c. Reverse the current group
            prev = groupNext
            curr = groupPrev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            # d. Reconnect the group
            tmp = groupPrev.next  # The original first node, now the tail
            groupPrev.next = kth  # Connect previous group to the new head
            groupPrev = tmp       # Prepare for the next group
            
        return dummy.next

    # b. HINT: Create getKth(curr, k) helper function
    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
