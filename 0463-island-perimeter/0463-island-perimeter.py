class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        visited = set()
        directions = [(1,0), (0, 1), (-1, 0), (0,-1)]
        
        def isInbound(index):
            row = index[0]
            col = index[1]
            return (0 <= row < len(grid)) and (0 <= col < len(grid[0]))
        
        count = 0
        def dfs(index):
            nonlocal count
            visited.add(index)

            for direction in directions:
                
                row = index[0] + direction[0]
                col = index[1] + direction[1]
                
                
                if (isInbound((row, col))) and ((row, col) not in visited) and (grid[row][col] == 1):
                    dfs((row, col))
                    
                elif ((row, col) not in visited):
                    count += 1
                
            
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    dfs((row, col))
                    return count