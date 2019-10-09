# -*- coding: utf-8 -*-
"""
@author: Nicotine
@time: 2019/10/9 上午8:25
@desc: Bigo
"""


def bubble_sort(nums):
    for i in range(len(nums)-1):
        for j in range(len(nums)-1-i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums


array = [3, 2, 1, 15, 26, 72, 36, 10]
print(bubble_sort(array))
