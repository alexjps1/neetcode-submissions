# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(None, None)
        cur = head
        ptr1 = list1
        ptr2 = list2
        while ptr1 is not None or ptr2 is not None:
            if (ptr1 and ptr2 and ptr1.val < ptr2.val) or ptr2 is None:
                cur.next = ptr1
                ptr1 = ptr1.next
                cur = cur.next
            else:
                cur.next = ptr2
                ptr2 = ptr2.next
                cur = cur.next
        return head.next

        