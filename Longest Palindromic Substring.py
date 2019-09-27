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

    def longestPalindrome2(self, s):
        new_string = ""
        for i in range(len(s)):
            new_string += "#"
            new_string += s[i]
        new_string += "#"
        res = ""
        for i in range(len(new_string)):
            temp = self.helper(new_string, i, i)
            if len(temp) > len(res):
                res = temp
        return "".join([i for i in res if i != "#"])


if __name__ == "__main__":
    s = 'babad'
    print(Solution().longestPalindrome2(s))
    print(Solution().longestPalindrome2('ac'))
    print(Solution().longestPalindrome2('abb'))


