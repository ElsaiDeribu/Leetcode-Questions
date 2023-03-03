class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        
        prefRow1 = list(accumulate(grid[0]))
        prefRow2 = list(accumulate(grid[1]))
        
        n = len(grid[0])
        minimizedR2Score = float("inf")
        
        
        for i in range(n):
            
            upper = prefRow1[-1] - prefRow1[i]
            lower = prefRow2[i - 1]  if i > 0 else 0
            
            choiceOfR2 = max(upper, lower)
            minimizedR2Score = min(minimizedR2Score,  choiceOfR2)

            
        return  minimizedR2Score