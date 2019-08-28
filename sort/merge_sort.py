def merge_sort(nums):
    if len(nums) < 2:
        return nums
    mid = len(nums) // 2
    left = nums[:mid]
    right = nums[mid:]
    return merge(merge_sort(left), merge_sort(right))


def merge(arr1, arr2):
    res = []
    while len(arr1) > 0 and len(arr2) > 0:
        if arr1[0] > arr2[0]:
            res.append(arr2.pop(0))
        else:
            res.append(arr1.pop(0))
    while len(arr1):
        res.append(arr1.pop(0))
    while len(arr2):
        res.append(arr2.pop(0))
    return res


array = [3, 2, 1, 15, 26, 72, 36, 10]
print(merge_sort(array))
