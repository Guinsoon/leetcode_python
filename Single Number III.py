class Solution:
    def singleNumber(self, nums):
        if not nums:
            return []
        nums.sort()
        res = []
        idx = 0
        while idx < len(nums)-1:
            if nums[idx] == nums[idx+1]:
                idx += 2

            else:
                res.append(nums[idx])
                idx += 1
        if idx == len(nums)-1:
            res.append(nums[-1])
        return res


if __name__ == "__main__":
    a = [1, 2, 1, 3, 2, 5]
    print(Solution().singleNumber(a))

