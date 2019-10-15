# -*- coding: utf-8 -*-
"""
@author: Nicotine
@time: 2019/10/15 上午8:43
@desc: Bigo
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def printListFromTailToHead(self, listNode):
        if not listNode:
            return []
        res = []
