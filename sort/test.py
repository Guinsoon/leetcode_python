def bubble_sort(nums):
    for i in range(len(nums)-1):
        for j in range(len(nums)-1-i):
            if nums[j] > nums[j+1]:
                nums[j+1], nums[j] = nums[j], nums[j+1]
    return nums


def insertion_sort(nums):
    for i in range(len(nums)-1, 0, -1):
        temp = nums[i]
        while nums[i-1] > temp:
            nums[i] = nums[i-1]
        nums[i] = temp
    return nums


def merge_sort(nums):
    if len(nums) < 2:
        return nums
    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])

    return merge(left, right)


def merge(l1, l2):
    res = []
    while l1 and l2:
        if l1[0] > l2[0]:
            res.append(l2.pop(0))
        else:
            res.append(l1.pop(0))
    while l1:
        res.append(l1.pop(0))
    while l2:
        res.append(l2.pop(0))
    return res


def quick_sort(nums, lo, hi):
    if lo < hi:
        mid = partition(nums, lo, hi)
        quick_sort(nums, lo, mid-1)
        quick_sort(nums, mid+1, hi)
    return nums


def partition(nums, lo, hi):
    pivot = lo
    index = pivot + 1
    for i in range(index, hi):
        if nums[i] < nums[pivot]:
            nums[i], nums[index] = nums[index], nums[i]
            index += 1
    nums[pivot], nums[index-1] = nums[index-1], nums[pivot]
    return index-1


array = [3, 2, 1, 15, 26, 72, 36, 10]
print(bubble_sort(array))
print(insertion_sort(array))
print(merge_sort(array))
print(quick_sort(array, 0, len(array)-1))

