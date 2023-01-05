class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        cols = [[0] * n for i in range(n)] 
        countOfPairs = 0
        
        
        for i in range(n):
            for j in range(n):
                cols[j][i] = grid[i][j]
        
        
        for i in range(len(grid)):
            grid[i] = tuple(grid[i])
            
            
        rowCount = Counter(grid)
    
    
        for col in cols:
            countOfPairs += rowCount[tuple(col)]
        
        
        return countOfPairs 