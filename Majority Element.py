class Solution:
    def majorityElement(self, nums):
        count = 0
        maj = 0
        for i in range(len(nums)):
            if count == 0:
                maj = nums[i]
            if maj == nums[i]:
                count += 1
            else:
                count -= 1
        return maj


if __name__ == "__main__":
    a = [3, 2, 3]
    print(Solution().majorityElement(a))
    b = [2, 2, 1, 1, 1, 2, 2]
    print(Solution().majorityElement(b))
