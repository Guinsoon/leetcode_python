# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def largestValues(self, root):
        if not root:
            return
        path = []
        self.dfs(root, path, 0)
        res = list(map(max, path))
        return res

    def dfs(self, root, res, level):
        if not root:
            return
        if len(res) == level:
            res.append([])
        res[level].append(root.val)
        self.dfs(root.left, res, level+1)
        self.dfs(root.right, res, level+1)


