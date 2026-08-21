# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        head = ListNode(None, head)
        l = r = head
        for i in range(n):
            r = r.next
        while r and r.next:
            r = r.next
            l = l.next
        if l.next == r:
            l.next = None
        else:
            l.next = l.next.next
        return head.next
        
        