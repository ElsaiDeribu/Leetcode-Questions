class Solution:
    def numDecodings(self, s: str) -> int:
        
        
        
        @cache
        def dp(idx):
            
            if idx >= len(s):
                return 1
            
            if int(s[idx]) == 0:
                return 0
            
            res1 = 0
            if idx + 1 < len(s) :
                comb = int(str(s[idx]) + str(s[idx + 1]))
                
                if 1 <= comb <= 26:
                    res1 = dp(idx + 2)
            
            return res1 + dp(idx + 1) 
            
            
        return dp(0)