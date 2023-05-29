class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        memo = {}
        def cal(n):
            
            if n in memo:
                return memo[n]
            
            if n < 0: return 0
            if n == 0: return cost[0]
            
            memo[n] = min(cal(n - 1), cal(n - 2)) + (cost[n] if n < len(cost) else 0)
            return memo[n]
            
        
        return cal(len(cost))
    
    
    
        
            
            
            
            