# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# use bfs with per-layer iteration
# save rightmost node from each layer

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        queue = deque()
        queue.append(root)
        lyr = []
        n = 1
        while n:
            for i in range(n):
                popped = queue.popleft()
                lyr.append(popped.val)
                if popped.left:
                    queue.append(popped.left)
                if popped.right:
                    queue.append(popped.right)
            res.append(lyr[-1])
            n = len(queue)
        return res

        