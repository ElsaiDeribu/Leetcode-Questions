class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        
        row_sums = defaultdict(int)
        col_sums = defaultdict(int)
        
        for i in range(len(grid)):
            row_sums[i] = sum(grid[i])
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                col_sums[j] += grid[i][j]
                
        diff = []
        
        
        for i in range(len(grid)):
            temp = []
            for j in range(len(grid[0])):
                oneRow = row_sums[i]
                oneCol = col_sums[j]
                zeroRow = len(grid) - oneRow
                zeroCol = len(grid[0]) - oneCol
                
                difference = oneRow + oneCol - zeroRow - zeroCol
                
                temp.append(difference)
                
            diff.append(temp)
            
        return diff
                