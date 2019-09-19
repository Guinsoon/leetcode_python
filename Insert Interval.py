# -*- coding: utf-8 -*-
"""
@author: Nicotine
@time: 2019/9/19 上午8:26
@desc: Bigo
"""
class Solution:
    def insert(self, intervals, newInterval):
        if not newInterval:
            return intervals
        res = []
        for item in intervals:
