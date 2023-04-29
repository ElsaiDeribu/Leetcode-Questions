class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        
        directions = [(0, 1),(0, -1),(-1, 0),(1, 0)]
        
        def isInbound(index):
            row = index[0]
            col = index[1]
            
            return 0 <= row < len(maze) and 0 <= col < len(maze[0])
        
        level = deque([entrance])
        visited = set()
        currLayer = 0
        
        
        while level:
            
            currLayer += 1
            for _ in range(len(level)):
                
                cell = level.popleft()
                
                for direction in directions:
                    row = cell[0] + direction[0]
                    col = cell[1] + direction[1]
                    
                    if isInbound((row, col)) and (row,col) not in visited and maze[row][col] == ".":
                        visited.add((row, col))
                        level.append([row, col])
                        
                    elif not isInbound((row, col)) and  [cell[0], cell[1]] != entrance:
                        return currLayer - 1
                    
                    
        return -1