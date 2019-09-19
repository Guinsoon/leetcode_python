# -*- coding: utf-8 -*-
"""
@author: Nicotine
@time: 2019/9/19 上午8:26
@desc: Bigo
"""


class Solution:
    def insert(self, intervals, newInterval):
        low = 0
        high = 0
        for item in intervals:
            if item[0] <= newInterval[0] <= item[1]:
                low = intervals.index(item)
            if item[0] <= newInterval[1] <= item[1]:
                high = intervals.index(item)
        min_item = min(newInterval[0], intervals[low[0]])
        max_item = max(newInterval[1], intervals[high[1]])

        res = []
        for item in intervals:
            if