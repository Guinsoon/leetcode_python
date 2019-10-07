# -*- coding: utf-8 -*-
"""
@author: Nicotine
@time: 2019/10/6 上午10:37
@desc: Bigo
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root):
        if not root:
            return True
        return self.helper(root.left, root.right)

    def helper(self, left, right):
        if not left or not right:
            return left == right
        if left.val != right.val:
            return False
        return self.helper(left.left, right.right) and self.helper(left.right, right.left)


if __name__ == "__main__":
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)

    node2.left = node1
    node2.right = node3

    print(Solution().isSymmetric(node2))
