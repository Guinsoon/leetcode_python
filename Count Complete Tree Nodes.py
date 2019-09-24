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