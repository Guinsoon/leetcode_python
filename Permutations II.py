# -*- coding: utf-8 -*-
"""
@author: Nicotine
@time: 2019/9/30 上午8:29
@desc: Bigo
"""


class Solution:
    def permuteUnique(self, nums):
        res = []
        self.dfs(res, [], nums)
        return res

    def dfs(self, res, temp, nums):
        if len(temp) == len(nums):
            res.append(temp[:])
        for i in range(len(nums)):
            temp.append(nums[i])
            self.dfs(res, temp, nums)
            temp.pop()


if __name__ == "__main__":
    print(Solution().permuteUnique([1, 1, 2]))
