# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumNumbers(self, root):
        res = []
        self.dfs(res, "", root)
        return sum(map(int, res))

    def dfs(self, res, out, node):
        if not node:
            return
        if node and not node.left and not node.right:
            res.append(out + str(node.val))
        self.dfs(res, out+str(node.val), node.left)
        self.dfs(res, out+str(node.val), node.right)
