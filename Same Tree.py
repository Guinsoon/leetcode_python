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
