# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        stack = [root]
        depths = {}
        while stack:
            # pop stack only when both children done and therefore depth calc'd
            node = stack[-1]
            if node.left:
                lh = depths.get(node.left, None)
                if lh is None:
                    stack.append(node.left)
                    continue
            else:
                lh = 0

            if node.right:
                rh = depths.get(node.right, None)
                if rh is None:
                    stack.append(node.right)
                    continue
            else:
                rh = 0

            if abs(lh - rh) > 1:
                return False

            depths[node] = max(lh, rh) + 1
            stack.pop()

        return True

            

