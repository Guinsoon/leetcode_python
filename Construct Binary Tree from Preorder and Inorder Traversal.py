# -*- coding: utf-8 -*-
"""
@author: Nicotine
@time: 2019/9/20 下午9:03
@desc: Bigo
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder, inorder):
        """
        TLE
        :param preorder:
        :param inorder:
        :return:
        """
        if not preorder or not inorder:
            return
        root = TreeNode(preorder[0])
        idx = inorder.index(preorder[0])
        root.left = self.buildTree([i for i in preorder if i in inorder[:idx]], inorder[:idx])
        root.right = self.buildTree([i for i in preorder if i in inorder[idx+1:]], inorder[idx+1:])
        return root

    def buildTree2(self, preorder, inorder):
        if not preorder or not inorder:
            return
        idx = inorder.index(preorder.pop(0))
        root = TreeNode(inorder[idx])
        root.left = self.buildTree(preorder, inorder[:idx])
        root.right = self.buildTree(preorder, inorder[idx + 1:])
        return root


if __name__ == "__main__":
    pre = [3, 9, 20, 15, 7]
    ino = [9, 3, 15, 20, 7]

    print(Solution().buildTree(pre, ino))



