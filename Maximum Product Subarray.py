class Solution:
    def maxProduct(self, nums):
        res = nums[0]
        max_res = res
        min_res = res
        for i in range(1, len(nums)):
            if nums[i] < 0:
                max_res, min_res = min_res, max_res

            max_res = max(nums[i], nums[i] * max_res)
            min_res = min(nums[i], nums[i] * min_res)

            res = max(res, max_res)
        return res


if __name__ == "__main__":
    print(Solution().maxProduct([2, 3, -2, 4]))
