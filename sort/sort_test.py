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
    Stable sort
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
    """
    Unstable sort
    Time Complexity: O(n2)
    Space Complexity: O(1)
    :param nums: raw array
    :return: sorted array
    """
    for i in range(len(nums)-1):
        min_idx = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[min_idx]:
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]
    return nums


def merge_sort(nums):
    """
    Stable sort
    Time Complexity: O(nlog2n)
    Space Complexity: O(n)
    :param nums: raw array
    :return: sorted array
    """
    if len(nums) < 2:
        return nums
    mid = len(nums) // 2
    return merge(merge_sort(nums[:mid]), merge_sort(nums[mid:]))


def merge(left, right):
    res = []
    while len(left) > 0 and len(right) > 0:
        if left[0] > right[0]:
            res.append(right.pop(0))
        else:
            res.append(left.pop(0))
    if left:
        res += left
    if right:
        res += right
    return res


def quick_sort(nums, low, high):
    """
    Unstable sort
    Time Complexity: O(nlog2n)
    Space Complexity: O(nlog2n)
    :param nums: raw array
    :param low:  left index of nums
    :param high:  right index of nums
    :return: sorted nums
    """
    if low < high:
        pivot = partition_first(nums, low, high)
        quick_sort(nums, low, pivot-1)
        quick_sort(nums, pivot+1, high)
    return nums


def partition_last(nums, left, right):
    """
    This function takes last element as pivot.
    :param nums: raw array
    :param left: left index of nums
    :param right: right index of nums
    :return: the index of pivot.
    """
    pivot = nums[right]
    index = left - 1
    for i in range(left, right):
        if nums[i] < pivot:
            index += 1
            nums[i], nums[index] = nums[index], nums[i]
    nums[index+1], pivot = pivot, nums[index+1]
    return index+1


def partition_first(nums, left, right):
    """
    The function takes first element as pivot.
    :param nums: raw array
    :param left: left index of nums
    :param right: right index of nums
    :return: the index of pivot
    """
    pivot = nums[left]
    index = left + 1
    for i in range(index, right+1):
        if nums[i] < pivot:
            nums[i], nums[index] = nums[index], nums[i]
            index -= 1
    nums[index-1], pivot = pivot, nums[index-1]
    return index-1


array = [3, 2, 1, 15, 26, 72, 36, 10]
print(bubble_sort(array))
print(insertion_sort(array))
print(selection_sort(array))
print(merge_sort(array))
print(quick_sort(array, 0, len(array)-1))



