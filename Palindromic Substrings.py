# -*- coding: utf-8 -*-
"""
@author: Nicotine
@time: 2019/9/28 上午10:22
@desc: Bigo
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        res = []
        self.dfs(s, res, "", 0)
        return res

    def dfs(self, s, res, temp, idx):
        res.append(temp)
        for i in range(idx, len(s)):
            temp += s[i]
            self.dfs(s, res, temp, idx+1)
            temp = temp[:-1]

    def is_palindromic(self, s):
        return s == s[::-1]


if __name__ == "__main__":
    s = 'abc'
    print(Solution().countSubstrings(s))

