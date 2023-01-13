class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        
        def findMax(index):
            maximum = grid[index[0]][index[1]]
            
            for direction in directions:
                row = direction[0] + index[0]
                col = direction[1] + index[1]
                
                maximum = max(maximum, grid[row][col])
                
            return maximum
        
        rowSize = len(grid) - 2
        colSize = len(grid[0]) - 2
        
        maxGrid = [[0] * colSize for _ in range(rowSize)]
        
        for row in range(1, len(grid) - 1):
            for col in range(1, len(grid[0]) - 1):
                maxGrid[row - 1][col -1] = findMax((row, col)) 
                
        return maxGrid