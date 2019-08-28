def insertion(nums):
    for i in range(1, len(nums)):
        pre = i-1
        cur = nums[i]
        while pre >= 0 and cur < nums[pre]:
            nums[pre+1] = nums[pre]
            pre -= 1
        nums[pre+1] = cur
    return nums


array = [3, 2, 1, 15, 26, 72, 36, 10]
print(insertion(array))

