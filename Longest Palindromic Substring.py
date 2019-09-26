# -*- coding: utf-8 -*-
"""
@author: Nicotine
@time: 2019/9/26 上午8:29
@desc: Bigo
"""


class Solution:
    def longestPalindrome(self, s):
        if not s:
            return
        is_same = [a == b for a, b in zip(s, s[::-1])]
        res = ''
        for i in range(len(is_same)):
            if is_same[i] is True:
                res += s[i]
        return res


if __name__ == "__main__":
    s = 'babad'
    print(Solution().longestPalindrome(s))
