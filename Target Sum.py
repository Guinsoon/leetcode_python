class Solution:
    def findTargetSumWays(self, nums, S):
        total = sum(nums)
        if total < S or (total + S) % 2 == 1:
            return 0
        target = (total + S) // 2
        dp = [0] * (target + 1)
        dp[0] = 1
        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] + dp[i - num]
        return dp[target]

    def findTargetSumWays2(self, nums, S):
        res = 0
        self.dfs(nums, res, 0, S)
        return res

    def dfs(self, nums, res, pos, remain):
        if len(nums) == pos:
            if remain == 0:
                res += 1
            else:
                return
        self.dfs(nums, res, pos+1, remain-nums[pos])
        self.dfs(nums, res, pos+1, remain+nums[pos])


if __name__ == "__main__":
    a = [1, 1, 1, 1, 1]
    s = 3
    print(Solution().findTargetSumWays2(a, s))



