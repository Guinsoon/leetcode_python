class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()
        res = []
        backtrack(res, [], 0, nums)
        return res


def backtrack(res, temp, ids, nums):
    res.append(temp[:])
    for i in range(ids, len(nums)):
        if i > ids and nums[i] == nums[i - 1]:
            continue
        temp.append(nums[i])
        backtrack(res, temp, i + 1, nums)
        temp.pop()
