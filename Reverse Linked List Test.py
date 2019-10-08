# -*- coding: utf-8 -*-
"""
@author: Nicotine
@time: 2019/10/8 上午8:58
@desc: Bigo
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head):
        if not head:
            return
        dummy = ListNode(0)
        dummy.next = head
        last = None
        cur = head
        while last:
            temp = cur.next
            cur.next = last
            last = cur
            cur = temp
        return dummy
