# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root, sum):
        res = []
        self.dfs(res, [], sum, root)
        return res

    def dfs(self, res, out, remain, root):
        if not root:
            return
        out.append(root.val)
        if not root.left and not root.right and root.val == remain:
            res.append(out[:])
        self.dfs(res, out, remain-root.val, root.left)
        self.dfs(res, out, remain-root.val, root.right)
        out.pop()



