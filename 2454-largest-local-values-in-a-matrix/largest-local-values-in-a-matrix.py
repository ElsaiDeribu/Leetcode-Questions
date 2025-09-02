class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:

        dir = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(-1,1),(1,-1),(-1,-1)]

        updates = []

        
        for r in range(1, len(grid) - 1):
            for c in range(1, len(grid) - 1):
                curr = grid[r][c]

                for d_r, d_c in dir:
                    row, col = r + d_r, c + d_c

                    curr = max(curr, grid[row][col])

                updates.append((r,c,curr))

        for r, c , val in updates:
            grid[r][c] = val
            
        grid = grid[1:len(grid) - 1]

        for i in range(len(grid)):
            grid[i] = grid[i][1:len(grid[i]) - 1]



        return grid



        