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

            lh = depths.get(node.left, None) if node.left else 0
            rh = depths.get(node.right, None) if node.right else 0

            if lh is not None and rh is not None:
                if abs(lh - rh) > 1:
                    return False

                depths[node] = max(lh, rh) + 1
                stack.pop()
            else:
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)

        return True

            

