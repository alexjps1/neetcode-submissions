"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nmap = {}
        cur = head
        while cur:
            nmap[cur] = Node(cur.val, None, None)
            cur = cur.next
        cur = head
        while cur:
            nmap[cur].next = nmap[cur.next] if cur.next else None
            nmap[cur].random = nmap[cur.random] if cur.random else None
            cur = cur.next
        return nmap[head] if head else None
