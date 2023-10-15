class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        
        @cache
        def dp(stps, curr):
            
            if curr >= arrLen or curr < 0:
                return 0
            
            if stps == 0:
                if curr == 0:
                    return 1
                
                return 0
            
            res1 = dp(stps - 1, curr + 1)
            res2 = dp(stps - 1, curr )
            res3 = dp(stps - 1, curr - 1)
            
            return res1 + res2 + res3
        
        return dp(steps, 0) % (10**9 + 7)
        