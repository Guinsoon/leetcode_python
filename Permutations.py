# -*- coding: utf-8 -*-
"""
@author: Nicotine
@time: 2019/9/30 上午8:41
@desc: Bigo
"""


class Solution:
    def permute(self, nums):
        res = []
        self.dfs(res, [], nums)
        return res

    def dfs(self, res, temp, nums):
        if len(temp) == len(nums):
            res.append(temp[:])
        for num in nums:
            if num not in temp:
                temp.append(num)
                self.dfs(res, temp, nums)
                temp.pop()
