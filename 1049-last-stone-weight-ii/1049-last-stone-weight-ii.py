class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        
        full = sum(stones)
        half = full // 2
        
        @cache
        def dp(idx, total):
            nonlocal full
            
            if total >= half or idx == len(stones):
                return abs(total - (full - total))
                
            take = dp(idx + 1, total + stones[idx])
            notTake = dp(idx + 1, total)
                
            return min(take, notTake)
        
        
        
        return dp(0, 0)
        

    
    
    
    
    