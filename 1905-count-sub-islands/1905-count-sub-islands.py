class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        
        isSub = True
        count = 0
        
        def isInbound(index): 
            row = index[0]
            col = index[1]
            
            return 0 <= row < len(grid2) and 0 <= col < len(grid2[0])
        
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        
        
        def dfs(index):
            nonlocal isSub
            
            grid2[index[0]][index[1]] = 0
            if grid1[index[0]][index[1]] != 1:
                isSub = False
                
            for direction in directions:
                row = index[0] + direction[0] 
                col = index[1] + direction[1]        
                
                if isInbound((row, col)) and grid2[row][col] == 1:
                    dfs((row, col))
                    
        
        for row in range(len(grid2)):
            for col in range(len(grid2[0])):
                
                if grid2[row][col] == 1:
                    dfs((row, col))
                    if isSub: 
                        count += 1
                    isSub = True
                    
        return count
        