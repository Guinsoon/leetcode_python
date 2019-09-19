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
        if newInterval[1] < intervals[0][1]:
            return [newInterval] + intervals
        if newInterval[0] > intervals[-1][0]:
            return intervals + [newInterval]
        res = []
        for item in intervals:
            if item[1] < newInterval[0]:
                res.append(item)
            elif item[0] > newInterval[1]:
                if newInterval not in res:
                    res.append(newInterval)
                res.append(item)
            elif item[0] < newInterval[0] < item[1]:



