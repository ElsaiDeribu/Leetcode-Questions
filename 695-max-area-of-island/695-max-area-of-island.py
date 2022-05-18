class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(0,1), (0,-1), (-1,0),(1,0)]
        
        visited = set()
        largestArea = 0
        self.area = 0
        
        def dfs(n):
            self.area += 1
            visited.add(n)
            for i in directions:
                coord = (n[0] + i[0], n[1] + i[1])
                if 0 <= coord[0] < len(grid) and 0 <= coord[1] < len(grid[0]) and coord not in visited and grid[coord[0]][coord[1]] == 1:
                    dfs(coord)
                        
                        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in visited:
                    dfs((i,j))
                    largestArea = max(self.area, largestArea)
                    self.area = 0
                    
        
        return largestArea
        