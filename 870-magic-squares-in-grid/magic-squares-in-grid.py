class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        

        def check(row,col):

            visited = set()

            for r in range(row - 1, row + 2):
                for c in range(col - 1, col + 2):
                    if (grid[r][c] in visited) or (grid[r][c] > 9) or (grid[r][c] < 1):
                        return False

                    visited.add(grid[r][c])

            diag1 = grid[row][col] + grid[row + 1][col + 1] + grid[row - 1][col - 1]
            diag2 = grid[row][col] + grid[row - 1][col + 1] + grid[row + 1][col - 1]

            row1 = grid[row - 1][col - 1] + grid[row - 1][col] + grid[row - 1][col + 1]
            row2 = grid[row][col - 1] + grid[row][col] + grid[row][col + 1]
            row3 = grid[row + 1][col - 1] + grid[row + 1][col] + grid[row + 1][col + 1]

            col1 = grid[row - 1][col - 1] + grid[row][col - 1] + grid[row + 1][col - 1]
            col2 = grid[row - 1][col] + grid[row][col] + grid[row + 1][col]
            col3 = grid[row - 1][col + 1] + grid[row][col + 1] + grid[row + 1][col + 1]



            return diag1 == diag2 == row1 == row2 == row3 == col1 == col2 == col3

        ans = 0
        for r in range(1, len(grid) - 1):
            for c in range(1, len(grid[0]) - 1):
                if check(r, c):
                    ans += 1

        return ans

        

            
