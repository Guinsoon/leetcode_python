class Solution:
    def search(self, nums, target):
        if not nums:
            return -1

        left = 0
        right = len(nums)-1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            if nums[right] > nums[mid]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1


if __name__ == "__main__":
    a = [4, 5, 6, 7, 0, 1, 2]
    print(Solution().search(a, 0))
