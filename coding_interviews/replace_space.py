# -*- coding: utf-8 -*-
"""
@author: Nicotine
@time: 2019/10/14 上午10:02
@desc: Bigo
"""


class Solution:
    def replaceSpace(self, s):
        n = s.count(' ')
        res = list(s)
        res += [0] * 2 * n
        p1 = len(s)-1
        p2 = len(res)-1
        while p1 != p2:




    def replaceSpace_slow(self, s):
        res = ""
        for item in s:
            if item == " ":
                res += "%20"
            else:
                res += item
        return res


if __name__ == "__main__":
    strings = "We are happy"
    print(Solution().replaceSpace(strings))
