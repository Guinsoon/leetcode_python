# -*- coding: utf-8 -*-
"""
@author: Nicotine
@time: 2019/10/5 下午8:29
@desc: Bigo
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p, q):
        res_p = self.inorder(p)
        res_q = self.inorder(q)
        return res_p == res_q

    def inorder(self, root):
        if not root:
            return
        stack = []
        res = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append(root.val)
            root = root.right
        return res


if __name__ == "__main__":
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)

    node1.left = node2
    node1.right = node3

    print(Solution().inorder(node1))
