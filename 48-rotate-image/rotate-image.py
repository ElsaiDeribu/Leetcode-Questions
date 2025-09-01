class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        for r in range(len(matrix)):
            for c in range(r, len(matrix[0])):
                matrix[r][c], matrix[c][r] =  matrix[c][r], matrix[r][c]

        for i in range(len(matrix)):
            matrix[i] = matrix[i][::-1]

