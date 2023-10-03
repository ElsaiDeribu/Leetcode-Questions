class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        
        def isInbound(idx):
            return 0 <= idx[0] < len(grid) and 0 <= idx[1] < len(grid[0])
        
        t = grid[0][0]
        heap = [(t, (0, 0))]
        visited = set((0,0))
        
        while heap:
            val, idx = heappop(heap)
            t = max(t, val)
            
            if idx[0] == len(grid) - 1 and idx[1] == len(grid[0]) - 1:
                break
            
            for direction in directions:
                row = idx[0] + direction[0]
                col = idx[1] + direction[1]
                
                if isInbound((row, col)) and (row, col) not in visited:
                    visited.add((row, col))
                    heappush(heap, (grid[row][col], (row, col)))
                    
                    
        return t