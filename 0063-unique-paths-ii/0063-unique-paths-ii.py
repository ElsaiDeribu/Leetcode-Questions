class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        
        directions = [(1,0), (0,1)]
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        def isInbound(index):
            return 0 <= index[0] < m and 0 <= index[1] < n
        
        @cache 
        def count(curr):
            row = curr[0]
            col = curr[1]
            
            if obstacleGrid[row][col] == 1:
                return 0
            
            if row == m - 1 and col == n - 1:
                return 1
            
            total = 0
            for direction in directions:
                row = curr[0] + direction[0]
                col = curr[1] + direction[1]
                
                if isInbound((row, col)) and obstacleGrid[row][col] != 1:
                    total += count((row, col))
                    
            return total
        
        
                
        return count((0,0))
        