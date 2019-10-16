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
        """
        Using stack
        :param listNode: input linked list
        :return: the value of reverse linked list
        """
        if not listNode:
            return []
        stack = []
        res = []
        while listNode:
            stack.append(listNode)
            listNode = listNode.next
        while stack:
            node = stack.pop()
            res.append(node.val)
        return res

    def printListFromTailToHead2(self, listNode):
        """
        Using recursion
        :param listNode: input linked list
        :return: the value of reverse linked list
        """
        pass


