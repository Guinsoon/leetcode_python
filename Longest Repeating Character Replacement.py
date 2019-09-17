from collections import Counter


class Solution:
    def characterReplacement(self, s, k):
        if not s:
            return 0
        lo = hi = 0
        counter = Counter()
        for hi in range(len(s)):
            counter[s[hi]] += 1
            max_count = counter.most_common(1)[0][1]
            if hi - lo - max_count + 1 > k:
                counter[s[lo]] -= 1
                lo += 1
        return hi - lo + 1


if __name__ == "__main__":
    print(Solution().characterReplacement("ABAB", 2))

