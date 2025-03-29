class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:

        dir = [(0,0), (0,1), (0,-1), (1,0), (-1,0), (1,1) ,(-1,-1), (-1,1), (1,-1)]
    
        for r in range(1, len(grid) - 1):
            for c in range(1, len(grid[0]) - 1):

                for d in dir:
                    grid[r - 1][c - 1] = max(grid[r - 1][c - 1], grid[r + d[0]][c + d[1]])
        

        return [grid[r][:len(grid[0]) - 2 ] for r in range(len(grid) - 2)  ]