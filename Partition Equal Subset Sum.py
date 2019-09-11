class Solution:
    def canPartition(self, nums):
        total = sum(nums)
        if total % 2 != 0:
            return False
        total //= 2

        dp = [False] * (total+1)
        dp[0] = True
        for num in nums:
            for i in range(total, num-1, -1):
                dp[i] = dp[i] or dp[i-num]
        return dp[-1]


if __name__ == "__main__":
    a = [1, 5, 11, 5]
    print(Solution().canPartition(a))

