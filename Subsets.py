class Solution:
    def subsets(self, nums):
        res = []
        temp = []
        self.backtrack(res, temp, 0, nums)
        return res

    def backtrack(self, res, out, idx, nums):
        res.append(out[:])
        for i in range(idx, len(nums)):
            out.append(nums[i])
            self.backtrack(res, out, i+1, nums)
            out.pop()


if __name__ == "__main__":
    nums = [1, 2, 3]
    print(Solution().subsets(nums))
