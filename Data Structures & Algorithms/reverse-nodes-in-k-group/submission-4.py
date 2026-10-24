# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # dummy node with linked list attached, with groupPrev also referencing the dummy node
        dummy = ListNode(0, head)
        groupPrev = dummy

        # stores the kth node in kth and checks if kth is empty
        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
          
            groupNext = kth.next

            # reverse the group
            prev = groupNext
            curr = groupPrev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            # makes the previous group point to the next group and sets groupPrev to the node right before the next group
            node1 = groupPrev.next
            groupPrev.next = kth
            groupPrev = node1

        return dummy.next

    # gets the kth node (the node at the end of the group)
    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr