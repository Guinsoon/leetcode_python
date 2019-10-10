# -*- coding: utf-8 -*-
"""
@author: Nicotine
@time: 2019/10/9 上午8:25
@desc: Bigo
"""


def bubble_sort(nums):
    """
    Stable sort
    Time Complexity：O(n2)
    Space Complexity: O(1)
    :param nums: raw array
    :return: sorted array
    """
    for i in range(len(nums)-1):
        for j in range(len(nums)-1-i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums


def insertion_sort(nums):
    """
    Unstable sort
    Time Complexity: O(n2)
    Space Complexity: O(1)
    :param nums: raw array
    :return: sorted array
    """
    n = len(nums)
    for i in range(1, n):
        cur = i
        pre = i - 1
        while pre >= 0 and nums[pre] > nums[cur]:
            nums[pre+1] = nums[pre]
            pre -= 1
        nums[pre+1] = nums[cur]
    return nums


def selection_sort(nums):
    min_idx = 0
    for i in range(len(nums)):
        for j in range(1, len(nums)):
            if nums[j] < nums[min_idx]:
                min_idx = j


array = [3, 2, 1, 15, 26, 72, 36, 10]
print(bubble_sort(array))
print(insertion_sort(array))

