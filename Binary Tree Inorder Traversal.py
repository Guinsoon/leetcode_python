# -*- coding: utf-8 -*-
"""
@author: Nicotine
@time: 2019/10/3 上午11:29
@desc: Bigo
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root):
        if not root:
            return
        res = []
        self.inorderTraversal(root.left)
        res.append(root.val)
        self.inorderTraversal(root.right)
        return res


if __name__ == "__main__":
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)

    node1.right = node2
    node2.left = node3

    print(Solution().inorderTraversal(node1))

