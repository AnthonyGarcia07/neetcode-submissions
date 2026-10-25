# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # dummy node with linked list attached
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = self.getkth(groupPrev, k)
            if not kth: # if kth node is empty, fewer than k nodes remain, so break
                break
            
            groupNext = kth.next

            # reverses the group
            prev = groupNext
            curr = groupPrev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            # makes dummy node point to the new head, and moves groupPrev to the original head to prepare for the next group
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
        return dummy.next

    # this gets the kth node, which is the node at the end of the group
    def getkth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -=1
        return curr
