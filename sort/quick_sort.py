def quick(nums, lo, hi):
    if lo < hi:
        mid = partition(nums, lo, hi)
        quick(nums, lo, mid-1)
        quick(nums, mid+1, hi)
    return nums


def partition(nums, left, right):
    pivot = left
    index = pivot + 1
    for i in range(index, right+1):
        if nums[i] < nums[pivot]:
            nums[i], nums[index] = nums[index], nums[i]
            index += 1
    nums[pivot], nums[index-1] = nums[index-1], nums[pivot]
    return index-1


array = [3, 2, 1, 15, 26, 72, 36, 10]
print(quick(array, 0, len(array)-1))

