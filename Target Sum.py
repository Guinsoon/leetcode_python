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
        """
        Time limit exceeded.
        :param nums:
        :param S:
        :return:
        """
        self.res = 0
        self.dfs(nums, 0, S)
        return self.res

    def dfs(self, nums, pos, remain):
        if len(nums) == pos:
            if remain == 0:
                self.res += 1
            # 这里的return比较重要，不能放在else里，只要是nums的长度等于pos就返回
            return
        self.dfs(nums, pos+1, remain-nums[pos])
        self.dfs(nums, pos+1, remain+nums[pos])

    def findTargetSumWays3(self, nums, S):
        total = sum(nums)
        if total < S or (total + S) % 2 == 1:
            return 0
        target = (S + total) // 2
        dp = [[0] * (target + 1) for _ in range(len(nums) + 1)]
        dp[0][0] = 1
        for i in range(1, len(nums) + 1):
            dp[i][0] = 1
        for i in range(1, len(nums) + 1):
            for j in range(target + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= nums[i - 1]:
                    dp[i][j] += dp[i - 1][j - nums[i - 1]]
        return dp[len(nums)][target]


if __name__ == "__main__":
    # a = [1, 1, 1, 1, 1]
    # s = 3
    # print(Solution().findTargetSumWays2(a, s))
    b = [1, 2, 3, 4, 5]
    t = 3
    print(Solution().findTargetSumWays(b, t))
    print(Solution().findTargetSumWays3(b, t))




