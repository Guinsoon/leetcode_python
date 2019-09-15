class Solution:
    def intersect(self, nums1, nums2):
        nums1.sort()
        nums2.sort()

        p1 = 0
        p2 = 0
        res = []
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] == nums2[p2]:
                res.append(nums1[p1])
                p1 += 1
                p2 += 1
            elif nums1[p1] > nums2[p2]:
                p2 += 1
            else:
                p1 += 1
        return res


if __name__ == "__main__":
    a = [1, 2, 2, 1]
    b = [2, 2]
    c = [4, 9, 5]
    d = [9, 4, 9, 8, 4]
    print(Solution().intersect(a, b))
    print(Solution().intersect(c, d))

