class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m, n = len(matrix), len(matrix[0])
        l, r = 0, m * n

        while l < r:
            mid = l + (r - l) // 2

            row = mid // n
            col = mid % n

            if matrix[row][col] < target:
                l = mid + 1
            else:
                r = mid


        return matrix[r // n][r % n] == target if r < m * n else False
        