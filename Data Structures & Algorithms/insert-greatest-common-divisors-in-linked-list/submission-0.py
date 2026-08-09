# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur.next is not None:
            a = cur.val
            b = cur.next.val
            cur.next = ListNode(val=math.gcd(a, b), next=cur.next)
            cur = cur.next.next
        return head