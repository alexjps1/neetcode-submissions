# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def height(self, node) -> Tuple[int, int]:
        if not node:
            return 0, 0
        mx = 0
        lh = 0
        if node.left: 
            lh, lm = self.height(node.left)
            lh += 1
            mx = max(mx, lm)
        rh = 0
        if node.right:
            rh, rm = self.height(node.right)
            rh += 1
            mx = max(mx, rm)
        mx = max(mx, lh + rh)
        return max(lh, rh), mx
        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.height(root)[1]

        