class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix:
            return False
        row, col = len(matrix), len(matrix[0])
        low, high = 0, row * col - 1
        while low <= high:
            mid = (low + high) // 2
            num = matrix[mid // col][mid % col]
            if num > target:
                high = mid - 1
            elif num < target:
                low = mid + 1
            else:
                return True


