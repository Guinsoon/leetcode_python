# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        while root:
            if root.val - p.val > 0 and root.val - q.val > 0:
                root = root.left
            elif root.val - p.val < 0 and root.val - q.val < 0:
                root = root.right
            else:
                return root
