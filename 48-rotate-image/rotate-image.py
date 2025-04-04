class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        def reverse(arr):
            l = 0
            r = len(arr) - 1

            while l <= r:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1
        
        for r in range(len(matrix)):
            for c in range(r, len(matrix[0])):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]


        for row in matrix:
            reverse(row)


        