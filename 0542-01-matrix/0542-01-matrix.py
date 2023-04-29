class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        
        level = deque([])
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        closest = defaultdict(int)
        visited = set()
        
        def isInbound(index):
            row = index[0]
            col = index[1]
            
            return 0 <= row < len(mat) and 0 <= col < len(mat[0])
        
        
        
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if mat[row][col] == 0:
                    visited.add((row, col))
                    level.append((row, col))
                    
        
        currLayer = 0
        
        while level:
            
            currLayer += 1
            for _ in range(len(level)):
                cell = level.popleft()
                
                
                for direction in directions:
                    row = cell[0] + direction[0]
                    col = cell[1] + direction[1]
                    
                    if isInbound((row, col)) and (row, col) not in visited:
                        if mat[row][col] == 1 and (row, col) not in closest:
                            closest[(row, col)] = currLayer
                          
                        visited.add((row, col))
                        level.append((row, col))
        
        
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if (row, col) in closest:
                    mat[row][col] = closest[(row, col)]
                    
                else:
                    mat[row][col] = 0
                    
                
                        
        return mat
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        