class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1)[::-1]:
            if nums[i] < nums[i+1]:
                idx = i+1
                for j in range(i+1, len(nums)):
                    if nums[i] < nums[j] < nums[idx]:
                        idx = j
                nums[i], nums[idx] = nums[idx], nums[i]
                nums[i+1:] = sorted(nums[i+1:])
                return
        nums.sort()

    def myself(self, nums):
        for i in range(len(nums)-1, 0, -1):
            if nums[i-1] < nums[i]:
                for j in range(len(nums)-1, i-1, -1):
                    if nums[j] > nums[i-1]:
                        nums[i-1], nums[j] = nums[j], nums[i-1]
                        nums[i:] = sorted(nums[i:])
                        return
        nums.sort()


if __name__ == "__main__":
    a = [1, 2, 3]
    Solution().nextPermutation(a)
    print(a)


