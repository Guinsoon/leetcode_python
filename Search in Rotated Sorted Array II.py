class Solution:
    def search(self, nums, target):
        if not nums:
            return False

        left = 0
        right = len(nums)-1

        while left < right:
            mid = left + (right-left) // 2
            if nums[mid] == target:
                return True
            if nums[mid] > nums[left]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False


if __name__ == "__main__":
    a = [2, 5, 6, 0, 0, 1, 2]
    print(Solution().search(a, 6))

