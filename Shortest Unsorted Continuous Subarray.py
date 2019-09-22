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
        pass



if __name__ == "__main__":
    a = [2, 6, 4, 8, 10, 9, 15]
    print(Solution().findUnsortedSubarray(a))
    b = [1, 3, 2, 2, 2]
    print(Solution().findUnsortedSubarray(b))
    c = [1, 2, 3, 3, 3]
    print(Solution().findUnsortedSubarray(c))






