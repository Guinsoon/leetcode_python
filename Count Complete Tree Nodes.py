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


if __name__ == "__main__":
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)

    node1.left = node2
    node1.right = node3

    node2.left = node4
    node2.right = node5

    node3.left = node6

    print(Solution().countNodes2(node1))
