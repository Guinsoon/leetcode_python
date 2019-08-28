from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        res = [[root.val]]
        queue = deque([root])
        while queue:
            cur = []
            for i in range(len(queue)):
                root = queue.popleft()
                if root.left:
                    cur.append(root.left.val)
                    queue.append(root.left)
                if root.right:
                    cur.append(root.right.val)
                    queue.append(root.right)
            if cur:
                res.append(cur)
        return res

    def levelOrder2(self, root):
        res = []
        self.dfs(res, root, 0)
        return res

    def dfs(self, res, root, level):
        if not root:
            return
        if level == len(res):
            res.append([])
        res[level].append(root.val)
        self.dfs(res, root.left, level+1)
        self.dfs(res, root.right, level+1)

