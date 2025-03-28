class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        row = len(matrix) - 1
        col = 0

        while 0 <= row < len(matrix) and 0 <= col < len(matrix[0]):

            if matrix[row][col] > target:
                row -= 1
            elif matrix[row][col] < target:
                col += 1
            else:
                return True