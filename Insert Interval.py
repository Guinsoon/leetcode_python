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
        # if newInterval[1] < intervals[0][0]:
        #     return [newInterval] + intervals
        # if newInterval[0] > intervals[-1][1]:
        #     return intervals + [newInterval]
        # if newInterval[0] < intervals[0][0] and newInterval[1] > intervals[-1][1]:
        #     return [newInterval]
        low = 0
        high = 0
        for item in intervals:
            if item[0] <= newInterval[0] <= item[1]:
                low = intervals.index(item)
            if item[0] <= newInterval[1] <= item[1]:
                high = intervals.index(item)
        min_item = min(newInterval[0], intervals[low][0])
        max_item = max(newInterval[1], intervals[high][1])

        res = []
        i = 0
        while i < len(intervals):
            if i < low or i > high:
                res.append(intervals[i])
                i += 1
            else:
                if i == low:
                    res.append([min_item, max_item])
                while i <= high:
                    i += 1
        return res

    def insert2(self, intervals, newInterval):



if __name__ == "__main__":
    a = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    b = [4, 8]
    print(Solution().insert(a, b))
