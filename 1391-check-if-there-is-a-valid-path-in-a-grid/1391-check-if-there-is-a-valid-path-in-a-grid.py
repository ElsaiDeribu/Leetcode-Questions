class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        
        endPoint = {1:["left","right"], 2:["above", "below"], 
              3:["left", "below"], 4:["below", "right"], 
              5:["left", "above"], 6:["above", "right"]}
        
        check = {"right":"left", "above":"below", "left":"right", "below":"above"}
        directions = {"below":(1,0),"right":(0,1),"above":(-1,0),"left":(0,-1)}
        
        def isInbound(index):
            row = index[0]
            col = index[1]
            
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        parent = {}
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                parent[(row, col)] = (row, col)
        
        def find(x):
            nonlocal parent
            
            if parent[x] == x:
                return x
            
            parent[x] = find(parent[x])
            
            return parent[x]
        
        
        def union(x, y):
            nonlocal parent
            
            repX = find(x)
            repY = find(y)
            
            if repX == repY:
                return True
            
            parent[repX] = repY
            
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                
                parentStreet = grid[row][col]
                
                for ep in endPoint[parentStreet]:
                    
                    r = row + directions[ep][0]
                    c = col + directions[ep][1]
                    
                    if isInbound((r,c)): 
                        street = grid[r][c]
                        
                        if check[ep] in endPoint[street]:
                            union((row, col), (r, c))
                    
            
        return union((0,0), (len(grid) - 1, len(grid[0]) - 1))
            
    
    
    
    
    
    
    
            
            
            