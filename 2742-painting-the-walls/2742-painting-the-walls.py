class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:

        
        @cache
        def dp(i, remain):
            
            if remain <= 0:
                return 0
            
            if i >= len(time):
                return float("inf")
            

            take = dp(i + 1, remain - 1 - time[i]) + cost[i]
            notTake = dp(i + 1, remain)
            
            return min(take, notTake)
        
        
        return dp(0, len(time))