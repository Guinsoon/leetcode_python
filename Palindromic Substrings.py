# -*- coding: utf-8 -*-
"""
@author: Nicotine
@time: 2019/9/28 上午10:22
@desc: Bigo
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        pass

    def myself(self, s):
        if not s:
            return 1
        res = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if self.is_palindromic(s[i:j+1]):
                    res += 1
        return res

    def is_palindromic(self, s):
        return s == s[::-1]


if __name__ == "__main__":
    s = 'abc'
    print(Solution().myself(s))
    print(Solution().myself("aaa"))


