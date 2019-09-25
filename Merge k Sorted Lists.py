# -*- coding: utf-8 -*-
"""
@author: Nicotine
@time: 2019/9/25 上午9:08
@desc: Bigo
"""
import heapq


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists):
        h = []
        for head in lists:
            while head:
                heapq.heappush(h, head.val)
                head = head.next
        dummy = ListNode(-1)
        head = dummy

        while h:
            head.next = ListNode(heapq.heappop(h))
            head = head.next
        return dummy.next
