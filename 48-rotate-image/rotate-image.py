class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        for r in range(len(matrix)):
            for c in range(r + 1, len(matrix[0])):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

        for row in matrix:
            n = len(row)
            for i in range((n + 1)// 2):
                row[i], row[n - i - 1] = row[n - i - 1], row[i]
