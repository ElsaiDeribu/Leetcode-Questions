class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m, n = len(matrix), len(matrix[0])
        L, R = 0, m * n - 1

        while L <= R:

            mid = L + (R - L) // 2

            r = mid // n
            c = mid % n

            if matrix[r][c] == target:
                return True

            if matrix[r][c] > target:
                R = mid - 1
            else:
                L = mid + 1

        return False
