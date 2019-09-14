class Solution:
    def combine(self, n, k):
        res = []
        self.dfs2(res, n, k, [], 1)
        return res

    def dfs(self, res, n, k, out, start):
        if k == 0:
            res.append(out[:])
            return
        for i in range(start, n-k+2):
            out.append(i)
            self.dfs(res, n, k-1, out, i+1)
            out.pop()

    def dfs2(self, res, n, k, out, start):
        if len(out) == k:
            res.append(out[:])
            return
        for i in range(start, n+1):
            out.append(i)
            self.dfs2(res, n, k, out, i+1)
            out.pop()


if __name__ == "__main__":
    print(Solution().combine(4, 2))
