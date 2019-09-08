
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root):
        res = []
        self.helper(res, root)
        return res

    def helper(self, res, node):
        if not node:
            return
        res.append(node.val)
        for item in node.children:
            self.helper(res, item)

