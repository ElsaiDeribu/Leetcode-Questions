class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        

        dirs = [(0,1), (1,0), (-1,0), (0,-1)]

        def is_inbound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])


        def dfs(row, col):
 
            grid[row][col] = 0

            res = 1
            for dr, dc in dirs:
                new_row = row + dr
                new_col = col + dc

                if is_inbound(new_row, new_col) and grid[new_row][new_col] == 1:
                    res += dfs(new_row, new_col)

            return res


        ans = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    ans = max(ans, dfs(row, col))

        return ans