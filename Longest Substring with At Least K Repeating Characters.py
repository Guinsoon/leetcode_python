from collections import Counter


class Solution:
    def longestSubstring(self, s, k):
        cnt = Counter(s)
        res = 0
        temp = 0
        for i in range(len(s)):
            if cnt[s[i]] >= k:
                temp += 1
                res = max(res, temp)
            else:
                res = max(res, temp)
                temp = 0
        return res

    def longestSubstring2(self, s, k):
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(t, k) for t in s.split(c))
        return len(s)


if __name__ == "__main__":
    s1 = "aaabb"
    s2 = "ababbc"
    s3 = "ababacb"
    # print(Solution().longestSubstring(s1, 3))
    print(Solution().longestSubstring(s3, 3))
    print(Solution().longestSubstring2(s3, 3))


