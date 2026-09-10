# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# dfs tracking max path val when inspecting each node
# count up on append

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        stack = [(root, -math.inf)]
        res = 1

        while stack:
            cur, pathmax = stack.pop()
            newmax = max(pathmax, cur.val)
            if cur.left:
                stack.append((cur.left, newmax))
                if cur.left.val >= newmax:
                    res += 1
            if cur.right:
                stack.append((cur.right, newmax))
                if cur.right.val >= newmax:
                    res += 1
        
        return res
            
            


        