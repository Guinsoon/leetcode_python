# -*- coding: utf-8 -*-
"""
@author: Nicotine
@time: 2019/9/30 上午8:29
@desc: Bigo
"""


class Solution:
    def permuteUnique(self, nums):
        res = []
        output = []
        self.dfs(res, [], nums)
        for item in res:
            ans = list(map(lambda x: nums[x], item))
            if ans not in output:
                output.append(ans)
        return output

    def dfs(self, res, temp, nums):
        if len(temp) == len(nums):
            res.append(temp[:])
            return
        for i in range(len(nums)):
            if i not in temp:
                temp.append(i)
                self.dfs(res, temp, nums)
                temp.pop()


if __name__ == "__main__":
    print(Solution().permuteUnique([1, 1, 2]))
