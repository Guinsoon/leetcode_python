def shell(nums):
    gap = len(nums) // 2
    while gap > 0:
        for i in range(gap, len(nums)):
            j = i
            cur = nums[i]
            while j - gap >= 0 and cur < nums[j-gap]:
                nums[j] = nums[j-gap]
                j -= gap
            nums[j] = cur
        gap = gap // 2
    return nums


array = [3, 2, 1, 15, 26, 72, 36, 10]
print(shell(array))

