class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:


        def check_diagonal(r, c):

            while 0 <= r + 1 < len(matrix) and 0 <= c + 1 < len(matrix[0]):

                if not matrix[r][c] == matrix[r + 1][c + 1]:
                    return False
                r += 1
                c += 1

            return True


        for r in range(len(matrix)):
            if not check_diagonal(r,0):
                return False

        for c in range(len(matrix[0])):
            if not check_diagonal(0,c):
                return False

        return True