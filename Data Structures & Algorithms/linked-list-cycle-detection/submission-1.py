# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        myset = set()
        cur = head
        while cur:
            if cur in myset:
                return True
            myset.add(cur)
            cur = cur.next
        return False
            
    
