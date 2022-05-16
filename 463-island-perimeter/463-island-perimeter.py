class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        def findIsland(matrix):
            for i in range(len(matrix)):
                for j in range(len(matrix[i])):
                    if matrix[i][j] == 1:
                        return(i,j)
                
        direction = [(1,0),(0,1),(-1,0),(0,-1) ]
        r, c = findIsland(grid)
        self.row, self.col = len(grid), len(grid[0])
        visited = set()
        self.perimeter = 0
         
        def dfs(r, c):
                visited.add((r, c))
                for i in direction:
                    coord = (r + i[0], c + i[1])
                    if (coord[0],coord[1]) not in visited:
                        if 0 <= coord[0] < self.row and 0 <= coord[1] < self.col and grid[coord[0]][coord[1]] == 1:
                            dfs(coord[0], coord[1])

                        elif self.row <= coord[0] or coord[0] < 0 or self.col <= coord[1] or coord[1]  < 0:
                            self.perimeter += 1
                            
                        elif grid[coord[0]][coord[1]] == 0:
                            self.perimeter += 1
                        
                
        dfs(r, c)
        return self.perimeter