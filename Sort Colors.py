# -*- coding: utf-8 -*-
"""
@author: Nicotine
@time: 2019/9/23 上午8:44
@desc: Bigo
"""


class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(1, len(nums)):
            pre = i - 1
            cur = nums[i]
            while pre >= 0 and cur < nums[pre]:
                nums[pre + 1] = nums[pre]
                pre -= 1
            nums[pre + 1] = cur

    def dutch_flag(self, nums):
        red, white, blue = 0, 0, len(nums)-1

        while white <= blue:
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1

            elif nums[white] == 1:
                white += 1

            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1


if __name__ == "__main__":
    a = [2, 0, 2, 1, 1, 0]
    Solution().sortColors(a)
    print(a)

