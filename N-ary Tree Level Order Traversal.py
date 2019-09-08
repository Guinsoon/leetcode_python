# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root):
        res = []
        self.dfs(res, root, 0)
        return res

    def dfs(self, res, node, level):
        if not node:
            return
        if len(res) == level:
            res.append([])
        res[level].append(node.val)
        for item in node.children:
            self.dfs(res, item, level+1)
