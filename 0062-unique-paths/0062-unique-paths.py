class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        directions = [(0,1),(1,0)]
        
        def inbound(index):
            return 0 <= index[0] < m and 0 <= index[1] < n
        
        memo = {}
        def dfs(curr): 
            
            if curr in memo:
                return memo[curr]
            
            if curr[0] == m - 1 and curr[1] == n - 1:
                return 1
            
            if not inbound(curr):
                return 0
            
            total = 0
            
            for r, c in directions:
                row = curr[0] + r
                col = curr[1] + c
                
                total += dfs((row, col))
                
            memo[curr] = total  
            
            return total
        
        
        return dfs((0,0))