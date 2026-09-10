# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# need to keep a max and min that indicates bounds for children

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = [(root, -math.inf, math.inf)]

        while stack:
            # deal with stack
            cur, minim, maxim = stack.pop()
            if not cur:
                continue
            stack.append((cur.left, minim, cur.val))
            stack.append((cur.right, cur.val, maxim))

            # validate cur node
            if not (minim < cur.val < maxim):
                return False
            
        return True



