class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        ans = 0
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]

        def is_inbound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        def dfs(row, col):
            
            grid[row][col] = "0"

            for dr, dc in dirs:
                new_row = row + dr
                new_col = col + dc

                if is_inbound(new_row, new_col) and grid[new_row][new_col] == "1":
                    dfs(new_row, new_col)


        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    dfs(row, col)
                    ans += 1

        return ans

