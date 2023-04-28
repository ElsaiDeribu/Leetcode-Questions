class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        if grid[0][0] == 1:
            return -1
        
        level = deque([(0,0)])
        directions = [(1, 0), (0, 1),(1, 1),(-1, 0), (0, -1), (-1, -1), (-1, 1), (1, -1)]
        destination = (len(grid) - 1, len(grid[0]) - 1)
        visited = set()
        currLevel = 0
    
        
        def isInbound(index):
            row = index[0]
            col = index[1]
            
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        
        while level:
            
            currLevel += 1
            for _ in range(len(level)):
                cell = level.popleft()
                if cell == destination and grid[cell[0]][cell[1]] == 0:
                    return currLevel
                
                for direction in directions:
                    row = cell[0] + direction[0]
                    col = cell[1] + direction[1]
                
                    if isInbound((row, col)) and ((row, col) not in visited) and (grid[row][col] == 0):
                        visited.add((row, col))
                        level.append((row, col))
                
                
        return -1