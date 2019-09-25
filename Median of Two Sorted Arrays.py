# -*- coding: utf-8 -*-
"""
@author: Nicotine
@time: 2019/9/25 上午8:29
@desc: Bigo
"""


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        import numpy as np
        return np.median(nums1 + nums2)


if __name__ == "__main__":
    a = [1, 3]
    b = [2]
    print(Solution().findMedianSortedArrays(a, b))
