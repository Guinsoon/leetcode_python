# -*- coding: utf-8 -*-
"""
@author: Nicotine
@time: 2019/9/30 上午8:29
@desc: Bigo
"""


class Solution:
    def permuteUnique(self, nums):
        res = []
        self.dfs(res, [], nums, 0)
        return res

    def dfs(self, res, temp, nums, idx):
        if temp not in res:
            res.append(temp[:])
        for i in range(idx, len(nums)):
            temp.append(nums[i])
            self.dfs(res, temp, nums, i+1)
            temp.pop()


if __name__ == "__main__":
    print(Solution().permuteUnique([1, 1, 2]))
