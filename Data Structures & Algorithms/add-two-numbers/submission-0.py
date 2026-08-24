# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = prev = ListNode(-1, None) 
        cur1 = l1
        cur2 = l2
        carry = 0

        while cur1 or cur2 or carry:
            res = 0
            res += cur1.val if cur1 else 0
            res += cur2.val if cur2 else 0
            res += carry
            if res > 9:
                carry = res // 10
                res = res % 10
            else:
                carry = 0
            prev.next = ListNode(res, None)
            if cur1:
                cur1 = cur1.next
            if cur2:
                cur2 = cur2.next
            prev = prev.next
        return dummy.next

