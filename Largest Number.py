from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums):
        nums = map(str, nums)

        def compareTo(a, b):
            if a + b >= b + a:
                return 1
            else:
                return -1

        nums = sorted(nums, key=cmp_to_key(compareTo), reverse=True)
        res = ''.join(nums)
        res = res.lstrip('0')
        return res if res else "0"
