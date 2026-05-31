class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        m = r // 2
        while m < r and (matrix[m][0] > target or matrix[m + 1][0] <= target):
            if matrix[m][0] > target:
                r = m - 1
            elif matrix[m][0] < target:
                l = m + 1
            else:
                return True
            m = l + (r - l) // 2

        l = 0
        r = len(matrix[m]) - 1
        m2 = r // 2
        while l <= r:
            if matrix[m][m2] > target:
                r = m2 - 1
            elif matrix[m][m2] < target:
                l = m2 + 1
            else:
                return True
            m2 = l + (r - l) // 2
            
        return False
        