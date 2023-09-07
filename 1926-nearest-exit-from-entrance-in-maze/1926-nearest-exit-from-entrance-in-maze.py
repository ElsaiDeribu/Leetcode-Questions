class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        layer = deque([entrance])
        visited = set()
        visited.add((entrance[0], entrance[1]))
        
        def isInbound(idx):
            return 0 <= idx[0] < len(maze) and 0 <= idx[1] < len(maze[0])
        
        steps = -1
        while layer:
            steps += 1
            for _ in range(len(layer)):
                cell = layer.popleft()
                for direction in directions:
                    row = cell[0] + direction[0]
                    col = cell[1] + direction[1]
                    
                    if isInbound((row,col)) and maze[row][col] == '.' and (row, col) not in visited:
                        visited.add((row, col))
                        layer.append([row, col])
                        
                    elif not isInbound((row,col)) and [cell[0], cell[1]] != entrance :
                        return steps 
                        
        return -1
        