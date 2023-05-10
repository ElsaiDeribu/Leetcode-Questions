class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        
        deq = deque([])
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        visited = set()
        
        
        def isInbound(index):
            row = index[0]
            col = index[1]
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    visited.add((row, col))
                    deq.append((row, col))
                    break
            if deq:
                break
                
                
        starters = []
        while deq:
            
            for i in range(len(deq)):
                cell = deq.popleft()
                starters.append(cell)
                
                for direction in directions:
                    row = direction[0] + cell[0]
                    col = direction[1] + cell[1]
                    
                    if isInbound((row, col)) and (row, col) not in visited and grid[row][col] == 1:
                        visited.add((row, col))
                        deq.append((row, col))
         
        
        distance = -1 
        deq = deque(starters)
        
        while deq:
            distance += 1
            for i in range(len(deq)):
                cell = deq.popleft()
                
                for direction in directions:
                    row = direction[0] + cell[0]
                    col = direction[1] + cell[1]
                    
                    if isInbound((row, col)) and (row, col) not in visited:
                        
                        if grid[row][col] == 0:
                            visited.add((row, col))
                            deq.append((row, col))
                            
                        elif grid[row][col] == 1:
                            
                            return distance
                
                
