class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        
        def isInbound(index):
            row = index[0]
            col = index[1]
            
            return 0 <= row < len(land) and 0 <= col < len(land[0])
        
        directions =[(0,1),(1,0),(0,1),(1,0)]
        
        endRow = 0
        endCol = 0
        
        def dfs(index):
            nonlocal endRow
            nonlocal endCol
            
            land[index[0]][index[1]] = 0
            
            endRow = max(endRow, index[0])
            endCol = max(endCol, index[1])
            
            for direction in directions:
                row = index[0] + direction[0]
                col = index[1] + direction[1]
                
                if isInbound((row, col)) and land[row][col] == 1:
                    dfs((row, col))
            
        
        
        ans = []
        for row in range(len(land)):
            for col in range(len(land[0])):
                
                if land[row][col] == 1:
                    farm = [row, col]
                    dfs((row, col))
                    farm.append(endRow)
                    farm.append(endCol)
                    ans.append(farm)
                    endRow = 0
                    endCol = 0
                    
                    
        return ans