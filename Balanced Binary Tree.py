# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root):
        self.balanced = True
        self.get_height(root)
        return self.balanced

    def get_height(self, root):
        if not root:
            return 0
        left = self.get_height(root.left)
        right = self.get_height(root.right)
        if abs(left-right) > 1:
            self.balanced = False
        return max(left, right) + 1
