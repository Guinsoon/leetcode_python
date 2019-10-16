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
        res = []
        self.dfs(listNode, res)
        return res

    def dfs(self, listNode, res):
        if listNode:
            if listNode.next:
                self.dfs(listNode.next, res)
            res.append(listNode.val)


if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)

    node1.next = node2
    node2.next = node3

    print(Solution().printListFromTailToHead2(node1))



