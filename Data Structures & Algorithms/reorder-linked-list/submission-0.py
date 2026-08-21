# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle point (first node of second half)
        s = head
        f = head.next
        while f and f.next:
            s = s.next
            f = f.next.next
        head2 = s.next
        s.next = None

        # reverse second half
        pre = None
        cur = head2
        while cur:
            nex = cur.next
            cur.next = pre
            pre = cur
            cur = nex

        # pre is now head2
        head2 = pre

        # zip
        p1, p2 = head, head2
        while p2:
            n1, n2 = p1.next, p2.next
            p1.next = p2
            p2.next = n1
            p1, p2 = n1, n2

