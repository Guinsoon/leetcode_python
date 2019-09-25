# -*- coding: utf-8 -*-
"""
@author: Nicotine
@time: 2019/9/25 上午8:29
@desc: Bigo
"""


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        result = self.merge(nums1, nums2)
        if len(result) % 2 != 0:
            return result[len(result) // 2]
        else:
            return (result[len(result) // 2-1] + result[len(result) // 2]) / 2

    def merge(self, nums1, nums2):
        res = []
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1
        if i < len(nums1):
            res += nums1[i:]
        elif j < len(nums2):
            res += nums2[j:]
        return res


if __name__ == "__main__":
    a = [1, 2]
    b = [3, 4]
    print(Solution().findMedianSortedArrays(a, b))
