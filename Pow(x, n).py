# -*- coding: utf-8 -*-
"""
@author: Nicotine
@time: 2019/10/2 上午9:05
@desc: Bigo
"""


class Solution:
    def myPow(self, x, n):
        if n == 0:
            return 1
        if n == 1:
            return x
        if n < 0:
            return self.myPow(1/x, -n)
        return self.myPow(x, n-1) * x


if __name__ == "__main__":
    print(Solution().myPow(2.1, 3))
    print(Solution().myPow(2, -2))

