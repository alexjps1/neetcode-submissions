# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        seen = {}
        cur = head = ListNode(None, head)
        i = 0
        while cur:
            seen[i] = cur
            cur = cur.next
            i += 1
        seen[i-n-1].next = seen[i-n].next
        return head.next
        