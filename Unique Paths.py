from functools import reduce


class Solution:
    def uniquePaths(self, m, n):
        if m == 1 or n == 1:
            return 1

        if m <= n:
            up = m - 1
        else:
            up = n - 1
        down = m + n - 2

        denominator = reduce(lambda x, y: x*y, range(1, up+1)) * reduce(
            lambda x, y: x*y, range(1, down-up+1))
        numerator = reduce(lambda x, y: x*y, range(1, down+1))
        return int(numerator / denominator)

    def uniquePathsTwo(self, m, n):
        dp = [1 for i in range(n)]
        for i in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j - 1]
        return dp[n - 1]

    def uniquePathThree(self, m, n):
        if m < n:
            small = m
        else:
            small = n
        nume = 1
        deno = 1

        for i in range(1, small):
            deno *= i
            nume *= m+n-1-i

        return nume // deno


if __name__ == "__main__":
    a = 7
    b = 3
    print(Solution().uniquePaths(a, b))
