class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        
        @cache
        def dp(stps, curr):
      
            if stps == 0:
                if curr == endPos:
                    return 1
                return 0
            
            res1 = dp(stps - 1, curr + 1)
            res2 = dp(stps - 1, curr - 1)
            
            return res1 + res2 
        
        return dp(k, startPos) % (10**9 + 7)
        
        