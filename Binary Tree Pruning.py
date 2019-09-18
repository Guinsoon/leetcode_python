# -*- coding: utf-8 -*-
"""
@author: Nicotine
@time: 2019/9/18 上午10:02
@desc: Bigo
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pruneTree(self, root):
        if not root:
            return
        if root and not root.left and not root.right and root.val == 0:
            return
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        return root


if __name__ == "__main__":
    node1 = TreeNode(1)
    node2 = TreeNode(0)
    node3 = TreeNode(0)
    node4 = TreeNode(1)

    node1.right = node2
    node2.left = node3
    node2.right = node4

    print(Solution().pruneTree(node1))

