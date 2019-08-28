def selection(nums):
    for i in range(len(nums)-1):
        min_idx = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[min_idx]:
                min_idx = j

        nums[i], nums[min_idx] = nums[min_idx], nums[i]
    return nums


array = [3, 2, 1, 15, 26, 72, 36, 10]
print(selection(array))
