class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        
        satisfaction.sort()
        
        @cache
        def dp(time, idx ):
            if idx >= len(satisfaction):
                return 0
            
            
            take = dp(time + 1, idx + 1) + (time * satisfaction[idx])
            notTake = dp(time, idx + 1)
            
            return max(take, notTake)
        
        
        return dp(1, 0)