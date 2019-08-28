class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        if obstacleGrid[-1][-1] == 1:
            return 0
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * m for _ in range(n)]
        for i in range(m):
            if obstacleGrid[0][i] != 1:
                dp[0][i] = 1
            else:
                break
        for j in range(n):
            if obstacleGrid[j][0] != 1:
                dp[j][0] = 1
            else:
                break
        if obstacleGrid[0][0] == 0:
            dp[0][0] = 1
        else:
            dp[0][0] = 0
        for i in range(1, n):
            for j in range(1, m):
                if obstacleGrid[i - 1][j] == 1:
                    dp[i - 1][j] = 0
                if obstacleGrid[i][j - 1] == 1:
                    dp[i][j - 1] = 0
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]


if __name__ == "__main__":
    a = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]]
    print(Solution().uniquePathsWithObstacles(a))
    b = [[0, 0], [1, 1], [0, 0]]
    print(Solution().uniquePathsWithObstacles(b))
    c = [[0]]
    print(Solution().uniquePathsWithObstacles(c))


