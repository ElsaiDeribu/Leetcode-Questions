class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:

    
        for r in range(1, len(grid) - 1):
            for c in range(1, len(grid[0]) - 1):

                for i in range(r - 1, r + 2):
                    for j in range( c - 1, c + 2):

                        grid[r - 1][c - 1] = max(grid[r - 1][c - 1], grid[i][j])
        

        return [grid[r][:len(grid[0]) - 2 ] for r in range(len(grid) - 2) ]