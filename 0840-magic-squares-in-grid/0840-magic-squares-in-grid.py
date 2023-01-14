class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        
        
        def checkMagic(center):
            r = center[0]
            c = center[1]
            sectionElements = set()
            directions = [(-1,0), (0,-1), (0,0), (0,1), (1,0), (-1,-1), (1,1), (-1,1), (1,-1)]
            for direction in directions:
                row = center[0] + direction[0]
                col = center[1] + direction[1]
                
                if grid[row][col] in sectionElements or grid[row][col] > 9 or grid[row][col] < 1:
                    return False
                
                sectionElements.add(grid[row][col])

            row1 = grid[r - 1][c - 1] + grid[r - 1][c] + grid[r - 1][c + 1]
            row2 = grid[r][c - 1] + grid[r][c] + grid[r][c + 1]
            row3 = grid[r + 1][c - 1] + grid[r + 1][c] + grid[r + 1][c + 1]
            
            col1 = grid[r + 1][c - 1] + grid[r][c - 1] + grid[r - 1][c - 1]
            col2 = grid[r + 1][c] + grid[r][c] + grid[r - 1][c]
            col3 = grid[r + 1][c + 1] + grid[r][c + 1] + grid[r - 1][c + 1]
            
            diagonal1 = grid[r + 1][c + 1] + grid[r][c] + grid[r - 1][c - 1]
            diagonal2 = grid[r + 1][c - 1] + grid[r][c] + grid[r - 1][c + 1]
            
            print(row1, row2, row3, col1, col2, col3, diagonal1, diagonal2)
            if row1 == row2 == row3 == col1 == col2 == col3 == diagonal1 == diagonal2:
                return True
            
            return False
            
        magicCount = 0  
        
        for row in range(1, len(grid) - 1):
            for col in range(1, len(grid[0]) - 1):
                if checkMagic((row, col)):
                    magicCount += 1
                    
                    
        return magicCount