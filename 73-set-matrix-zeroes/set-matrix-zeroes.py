class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        first_row_has_0 = False
        first_col_has_0 = False

        for r in range(len(matrix)):
            if matrix[r][0] == 0:
                first_col_has_0 = True
                break

        for c in range(len(matrix[0])):
            if matrix[0][c] == 0:
                first_row_has_0 = True


        for r in range(1, len(matrix)):
            for c in range(1, len(matrix[0])):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        for r in range(1, len(matrix)):
            if matrix[r][0] == 0:
                for c in range(len(matrix[0])):
                    matrix[r][c] = 0

        for c in range(1, len(matrix[0])):
            if matrix[0][c] == 0:
                for r in range(len(matrix)):
                    matrix[r][c] = 0


        if first_row_has_0:
            for c in range(len(matrix[0])):
                matrix[0][c] = 0

        if first_col_has_0:
            for r in range(len(matrix)):
                matrix[r][0] = 0


        


