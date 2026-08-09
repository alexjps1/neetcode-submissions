# tried for 15 min but didn't get it
# annotated solution

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # null case
        if not head:
            return head
        
        # count list length and get to the end of the list
        cur, n = head, 1
        while cur.next:
            n += 1
            cur = cur.next

        # glue the beginning to the end
        cur.next = head

        # fix # list rotations greater than list length
        k %= n

        # use n-k to turn left rotations to right rotations
        for i in range(n-k):
            cur  = cur.next

        # now we're at the new list end
        head = cur.next
        cur .next = None
        return head


        