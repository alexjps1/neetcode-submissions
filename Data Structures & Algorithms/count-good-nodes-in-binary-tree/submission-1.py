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
        stack = [(root, -math.inf)]
        res = 0

        while stack:
            cur, pathmax = stack.pop()
            if not cur:
                continue
            if cur.val >= pathmax: res += 1
            newmax = max(pathmax, cur.val)
            stack.append((cur.left, newmax))
            stack.append((cur.right, newmax))

        return res
            
            


        