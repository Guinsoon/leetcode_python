# -*- coding: utf-8 -*-
"""
@author: Nicotine
@time: 2019/10/14 下午6:42
@desc: Bigo
"""


class Solution:
    def Find(self, target, array):
        if not target:
            return False
        r = len(array)
        c = len(array[0])
        i = 0
        j = c - 1
        while i < r and j >= 0:
            if target == array[i][j]:
                return True
            elif target < array[i][j]:
                j -= 1
            elif target > array[i][j]:
                i += 1
        return False


if __name__ == "__main__":
    nums = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]
    item = 7
    print(Solution().Find(item, nums))
