class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        m, n = len(grid), len(grid[0])
        direcs = [(0,1),(1,0),(-1,0),(0,-1)]
        ans = 0


        def is_inbound(r, c):
            return 0 <= r < m and 0 <= c < n

        def dfs(r, c):

            grid[r][c] = "0"

            for dr, dc in  direcs:
                nr, nc = dr + r, dc + c

                if is_inbound(nr, nc) and grid[nr][nc] == "1":
                    dfs(nr, nc)
    
                
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    ans += 1
                    dfs(row,col)

        return ans







        