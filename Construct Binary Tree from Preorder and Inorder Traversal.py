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
        root = TreeNode(preorder[0])
        idx = inorder.index(preorder[0])
        root.left = self.buildTree([i for i in inorder[:idx] if i in preorder], inorder[:idx])
        root.right = self.buildTree([i for i in inorder[idx:] if i in preorder], inorder[idx:])
        return root


