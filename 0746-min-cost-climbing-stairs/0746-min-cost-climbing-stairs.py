class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        memo = {}
        def cal(n):
            
            if n in memo:
                return memo[n]
            
            if n >= len(cost):
                return 0
            
            if n == len(cost) - 1:
                return cost[-1]
            
            
            res1 = cal(n + 1)
            res2 = cal(n + 2)
            
            memo[n] = min(res1, res2) + cost[n]
            return memo[n]
        
        
        return min(cal(0), cal(1))
            
            
            
            