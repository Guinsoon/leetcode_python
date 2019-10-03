# -*- coding: utf-8 -*-
"""
@author: Nicotine
@time: 2019/10/3 上午11:36
@desc: Bigo
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root):
        if not root:
            return False
        return (root.left and root.left.val <= root.val) or\
               (root.right and root.right.val >= root.val) and\
               self.isValidBST(root.left) and self.isValidBST(root.right)

    def inorder(self, root):
        if not root:
            return True
        stack = []
        pre = None
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if pre and pre.val >= root.val:
                return False
            pre = root
            root = root.right
        return True


if __name__ == "__main__":
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)

    node2.left = node1
    node2.right = node3

    print(Solution().isValidBST(node2))

