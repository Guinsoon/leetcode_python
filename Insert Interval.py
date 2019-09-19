# -*- coding: utf-8 -*-
"""
@author: Nicotine
@time: 2019/9/19 上午8:26
@desc: Bigo
"""


class Solution:
    def insert(self, intervals, newInterval):
        if not intervals:
            return [newInterval]
        low = -1
        high = len(intervals)
        res = []
        for item in intervals:
            if item[0] <= low <= item[1]:
                low = intervals.index(item)
            if item[0] <= high <= item[1]:
                high = intervals.index(item)
        if low == -1 and high == len(intervals):
            if newInterval[1] < intervals[0][0]:
                return [newInterval] + intervals
            elif newInterval[0] > intervals[-1][1]:
                return intervals + [newInterval]
            else:
                return [newInterval]
        if low == -1 and high < len(intervals):
            res.append([newInterval[0], max(intervals[high][1], newInterval[1])])
            while high < len(intervals)-1:
                res.append(intervals[high])
                high += 1
            return res
        if low > -1 and high == len(intervals):
            i = 0
            while i < low:
                res.append(intervals[i])
            res.append([min(intervals[low][0], newInterval[0]), newInterval[1]])
            return res


if __name__ == "__main__":
    a = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    b = [4, 8]
    print(Solution().insert(a, b))
