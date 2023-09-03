class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        
        directions = [(1,0), (0,1)]
        m = len(grid)
        n = len(grid[0])
        
        def isInbound(index):
            return 0 <= index[0] < m and 0 <= index[1] < n
        
        @cache 
        def count(curr):
            row = curr[0]
            col = curr[1]
            
            if row == m - 1 and col == n - 1:
                return grid[row][col]
            
            total = float("inf")
            for direction in directions:
                row = curr[0] + direction[0]
                col = curr[1] + direction[1]
                
                if isInbound((row, col)):
                    total = min(total, count((row, col)))
                    
            return total + grid[curr[0]][curr[1]]
        
        
                
        return count((0,0))