class Solution:
    def minSteps(self, n: int) -> int:
        
        @cache
        def dp(paste, size, clip): 
             
            if size > n or clip > n:
                return float("inf")
            
            if size == n or n == 1:
                return 0
            
            if not paste: 

                res1 = dp(not paste, size + clip, clip)
                return res1 + 1
            else:
                
                res2 = min(dp(paste,size + clip, clip), dp(not paste, size, size))
                return res2 + 1
            
            
        return dp(False,0,1)
            
                
