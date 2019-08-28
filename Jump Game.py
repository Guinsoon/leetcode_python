class Solution:
    def canJump(self, nums):
        reach = 0
        for i in range(len(nums)):
            if reach >= len(nums)-1 or i > reach:
                break
            else:
                reach = max(i + nums[i], reach)
        return reach >= len(nums)-1


if __name__ == "__main__":
    a = [2, 3, 1, 1, 4]
    print(Solution().canJump(a))
