# -*- coding: utf-8 -*-
"""
@author: Nicotine
@time: 2019/9/21 下午2:11
@desc: Bigo
"""


class Solution:
    def findUnsortedSubarray(self, nums):
        if not nums:
            return 0
        start = None
        end = None
        for i in range(len(nums)-1):
            if nums[i+1] < nums[i]:
                if start is None:
                    start = i
                end = i + 1

        if start is None:
            return len(nums)
        else:
            return end-start+1

i


