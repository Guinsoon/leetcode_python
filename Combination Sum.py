class Solution:
    def combinationSum(self, candidates, target):
        candidates.sort()
        res = []
        temp = []
        backtrack(res, temp, candidates, target, 0)
        return res


def backtrack(res, out, nums, remain, start):
    if remain < 0:
        return
    if remain == 0:
        res.append(out[:])
    else:
        for i in range(start, len(nums)):
            out.append(nums[i])
            backtrack(res, out, nums, remain-nums[i], i)
            out.pop()


if __name__ == "__main__":
    a = [2, 3, 6, 7]
    target = 7
    print(Solution().combinationSum(a, target))
