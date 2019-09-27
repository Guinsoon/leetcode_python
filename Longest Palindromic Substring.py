# -*- coding: utf-8 -*-
"""
@author: Nicotine
@time: 2019/9/26 上午8:29
@desc: Bigo
"""


class Solution:
    def longestPalindrome(self, s):
        res = ""
        for i in range(len(s)):
            temp = self.helper(s, i, i)
            if len(temp) > len(res):
                res = temp
            temp = self.helper(s, i, i+1)
            if len(temp) > len(res):
                res = temp
        return res

    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1: r]


if __name__ == "__main__":
    s = 'babad'
    print(Solution().longestPalindrome(s))
    print(Solution().longestPalindrome('ac'))
    print(Solution().longestPalindrome('abb'))


