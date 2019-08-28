class Solution:
    def findLength(self, A, B):
        m, n = len(A), len(B)
        res = 0
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                if A[i] == B[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                    res = max(res, dp[i+1][j+1])
        return res


if __name__ == "__main__":
    a = [1, 2, 3, 2, 1]
    b = [3, 2, 1, 4, 7]
    print(Solution().findLength(a, b))
