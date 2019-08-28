# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root):
        res = []
        self.dfs(res, root, 0)
        return res

    def dfs(self, res, root, level):
        if not root:
            return
        if level == len(res):
            res.append([])
        if level % 2 == 0:
            res[level].append(root.val)
        else:
            res[level].insert(0, root.val)
        self.dfs(res, root.left, level + 1)
        self.dfs(res, root.right, level + 1)
