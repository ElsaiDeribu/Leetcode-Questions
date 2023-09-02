class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        
        @cache
        def dp(idx):
            
            if idx >= len(s):
                return 0
                
            res = float("inf")
            for i in range(idx, len(s)):
                temp = s[idx: i + 1]
                
                if temp in dictionary:
                    res = min(res,dp(i + 1)) 
                    
                else:
                    res = min(res, dp(i + 1) + len(temp))
            
            return res
        
        
        return dp(0)
        
        
        
                
                
                
                