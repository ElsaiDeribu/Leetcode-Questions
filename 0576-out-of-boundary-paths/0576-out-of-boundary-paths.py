class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
    
    
        def isInbound(index):
            row, col = index
            return 0 <= row < m and 0 <= col < n
        
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        
        @cache 
        def explore(index, moves):
            if not isInbound(index):
                return 1
            if moves == 0:
                return 0
             
            paths = 0
            
            for direction in directions:
                row = index[0] + direction[0]
                col = index[1] + direction[1]
                paths += explore((row, col), moves - 1)
                
            return paths
        
        mod = 10**9 + 7
        return explore((startRow, startColumn), maxMove) % mod
    
    
    