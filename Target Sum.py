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


if __name__ == "__main__":
    a = [1, 1, 1, 1, 1]
    s = 3
    print(Solution().findTargetSumWays(a, s))



