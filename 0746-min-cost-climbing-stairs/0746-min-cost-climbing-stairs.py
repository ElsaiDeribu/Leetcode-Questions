class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        @cache
        def cal(n):
            
            if n >= len(cost):
                return 0
            
            if n == len(cost) - 1:
                return cost[-1]
            
            
            res1 = cal(n + 1)
            res2 = cal(n + 2)
            
            return min(res1, res2) + cost[n]
        
        
        return min(cal(0), cal(1))
            
            
            
            