from collections import Counter


class Solution:
    def longestSubstring(self, s, k):
        """
        Wrong answer
        :param s:
        :param k:
        :return:
        """
        cnt = Counter(s)
        res = 0
        temp = 0
        for i in range(len(s)):
            if cnt[s[i]] >= k:
                temp += 1
            else:
                temp = 0
            res = max(res, temp)
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
    print(Solution().longestSubstring(s1, 3))
    print(Solution().longestSubstring(s3, 3))
    print(Solution().longestSubstring2(s3, 3))


