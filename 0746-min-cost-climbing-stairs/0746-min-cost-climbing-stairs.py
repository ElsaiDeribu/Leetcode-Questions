class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        @cache
        def dp(curr):
            if curr >= len(cost):
                return 0
            
            return min(dp(curr + 1), dp(curr + 2)) + cost[curr]
        
        
        return min(dp(0), dp(1))