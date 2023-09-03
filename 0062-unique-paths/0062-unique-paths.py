class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        directions = [(1,0), (0,1)]
        
        def isInbound(index):
            return 0 <= index[0] < m and 0 <= index[1] < n
        
        @cache 
        def count(curr):
            row = curr[0]
            col = curr[1]
            
            if row == m - 1 and col == n - 1:
                return 1
            
            total = 0
            for direction in directions:
                row = curr[0] + direction[0]
                col = curr[1] + direction[1]
                
                if isInbound((row, col)):
                    total += count((row, col))
                    
            return total
        
        
                
        return count((0,0))