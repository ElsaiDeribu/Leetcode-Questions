class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:

        r, c = 0, 0
        ans = 0

        while r < len(mat) and c < len(mat[0]):

            ans += mat[r][c]
            r += 1
            c += 1


        r, c = 0, len(mat[0]) - 1

        while 0 <= c and r < len(mat):
            ans += mat[r][c]
            c -= 1
            r += 1

        if len(mat) % 2:
            ans -= mat[len(mat) // 2][len(mat[0]) // 2]

        return ans


        