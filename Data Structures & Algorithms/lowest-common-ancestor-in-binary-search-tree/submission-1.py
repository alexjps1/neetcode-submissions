# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def label(self, node: TreeNode, p: TreeNode, q: TreeNode):
        if node is None:
            return [0, 0]
        label = [0, 0]
        left = self.label(node.left, p, q)
        right = self.label(node.right, p, q)
        label[0] = left[0] or right[0]
        label[1] = left[1] or right[1]
        if node == p:
            label[0] = 1
        if node == q:
            label[1] = 1
        if label == [1, 1] and not self.res:
            self.res = node
        return label


    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.res = None
        self.label(root, p, q)
        return self.res
