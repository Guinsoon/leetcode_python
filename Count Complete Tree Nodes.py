# -*- coding: utf-8 -*-
"""
@author: Nicotine
@time: 2019/9/24 上午9:23
@desc: Bigo
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def countNodes(self, root):
        """
        bfs
        :param root:
        :return:
        """
        if not root:
            return 0
        queue = [root]
        res = []
        while queue:
            node = queue.pop(0)
            res.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return len(res)

    def countNodes2(self, root):
        """
        dfs
        compare the depth between left sub tree and right sub tree.
        A, If it is equal, it means the left sub tree is a full binary tree
        B, It it is not , it means the right sub tree is a full binary tree
        :param root:
        :return:
        """
        if not root:
            return 0
        left_depth = self.getDepth(root.left)
        right_depth = self.getDepth(root.right)
        if left_depth == right_depth:
            return pow(2, left_depth) + self.countNodes2(root.right)
        else:
            return pow(2, right_depth) + self.countNodes2(root.left)

    def getDepth(self, root):
        if not root:
            return 0
        return 1 + self.getDepth(root.left)
