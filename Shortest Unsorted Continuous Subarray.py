# -*- coding: utf-8 -*-
"""
@author: Nicotine
@time: 2019/9/21 下午2:11
@desc: Bigo
"""


class Solution:
    def findUnsortedSubarray(self, nums):
        """
        Wrong answer
        :param nums:
        :return:
        """
        if not nums:
            return 0
        start = None
        end = None
        for i in range(len(nums)-1):
            if nums[i+1] < nums[i]:
                if start is None:
                    start = i
                end = i + 1
            elif nums[i+1] == nums[i]:
                if start is not None:
                    end = i + 1

        if start is None:
            return 0
        else:
            return end-start+1

    def findUnsortedSubarray2(self, nums):
        is_same = [a == b for a, b in zip(nums, sorted(nums))]
        return 0 if all(is_same) else len(nums) - is_same.index(False) - is_same[::-1].index(False)

    def findUnsortedSubarray3(self, nums):
        end = -2
        start = -1
        min_num = nums[-1]
        max_num = nums[0]
        for i in range(1, len(nums)):
            max_num = max(max_num, nums[i])
            min_num = min(min_num, nums[len(nums)-1-i])
            if nums[i] < max_num:
                end = i
            if nums[len(nums)-1-i] > min_num:
                start = len(nums)-1-i
        return end-start+1


if __name__ == "__main__":
    a = [2, 6, 4, 8, 10, 9, 15]
    print(Solution().findUnsortedSubarray3(a))
    b = [1, 3, 2, 2, 2]
    print(Solution().findUnsortedSubarray3(b))
    c = [1, 2, 3, 3, 3]
    print(Solution().findUnsortedSubarray3(c))
    d = [1, 3, 2, 3, 3]
    print(Solution().findUnsortedSubarray3(d))







