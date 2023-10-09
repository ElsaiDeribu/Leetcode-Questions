class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        
        
        mod = 10 ** 9 + 7
        
        @cache
        def dp(length, sCost, prevMax):
            
            if length == 0:
                if sCost == 0:
                    return 1
                
                return 0
            
            res = 0
            for i in range(1, m + 1):
                
                if i > prevMax:
                    res += dp(length - 1, sCost - 1, i)
                    
                else:
                     res += dp(length - 1, sCost , prevMax)
        
            return res
        
        
        
        return dp(n, k, float("-inf") ) % mod