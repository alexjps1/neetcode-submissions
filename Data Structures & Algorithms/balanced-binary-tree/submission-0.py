# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def height(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        lh = self.height(root.left) if root.left else 0
        rh = self.height(root.right) if root.right else 0
        balanced = True if abs(lh - rh) <= 1 else False
        balanced = False if lh == -1 or rh == -1 else balanced
        return max(lh, rh) + 1 if balanced else -1
            
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return True if self.height(root) != -1 else False