# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a, b):
            while b > 0:
                a, b = b, a % b
            return a

        cur = head
        while cur.next is not None:
            a = cur.val
            b = cur.next.val
            cur.next = ListNode(val=gcd(a, b), next=cur.next)
            cur = cur.next.next
        return head