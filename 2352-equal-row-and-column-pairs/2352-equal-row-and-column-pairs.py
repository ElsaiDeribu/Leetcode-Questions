class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        
        count = 0
        
        def iterateOverCol(c):
            temp = []
            for k in range(len(grid)):
                temp.append(grid[k][c])
            return temp
        
        cols = []
        
        for i in range(len(grid)):
            cols.append(iterateOverCol(i))
        
        
        for j in range(len(grid)):
            for t in range(len(grid)):
                if grid[j] == cols[t]:
                    count += 1

            
        return count