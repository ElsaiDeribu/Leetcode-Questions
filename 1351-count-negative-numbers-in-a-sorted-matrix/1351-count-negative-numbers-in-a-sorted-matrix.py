class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        initial = len(grid[0]) - 1
        
        for i in range(len(grid)):
            for j in range(initial,-1, -1):
                print(j)
                if (grid[i][j] >= 0 ):
                    initial = j
                    count += (len(grid[0]) - j - 1)
                    break
                if j == 0:
                    count += len(grid[0])
                    
        return count
    
    
