class Solution:
    def integerBreak(self, n: int) -> int:
        
        
        @cache
        def dp(rem, idx):
            
            if rem == 0:
                return 1
            
            res = float(-inf)
            end =  rem + 1 if idx != 0 else rem
            for i in range(1, end):
                
                res =  max(res, i * dp(rem - i, idx + 1))
                          
                          
            return res
                         
                          
        return dp(n, 0)
                