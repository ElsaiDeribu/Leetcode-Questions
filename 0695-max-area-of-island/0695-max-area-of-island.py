class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        
        def inbound(index):
            row = index[0]
            col = index[1]
             
            return (0 <= row < len(grid)) and (0 <= col < len(grid[0]))
        
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        
        
        def getArea(index):
            
            total = 1
            grid[index[0]][index[1]] = 0
            
            for direction in directions:
                row = index[0] + direction[0]
                col = index[1] + direction[1]
                 
                if inbound((row, col)) and grid[row][col] == 1: 
                
                    total += getArea((row, col))
            
            return total
            
         
        mxArea = 0
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    mxArea = max(mxArea, getArea((row, col)))
            
          
        return mxArea