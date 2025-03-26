class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:

        ans = 0

        def checkSum(r, c):
            top = grid[r-1][c] + grid[r-1][c-1] + grid[r-1][c+1]
            center = grid[r][c]
            bottom = grid[r+1][c] + grid[r+1][c-1] + grid[r+1][c+1]

            return top + center + bottom


        for r in range(1, len(grid) - 1):
            for c in range(1, len(grid[0]) - 1):
                ans = max(checkSum(r, c), ans)

        return ans
        