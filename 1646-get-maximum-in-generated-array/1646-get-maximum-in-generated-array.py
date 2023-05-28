class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        
        ans = 0
        
        memo = {}
        
        def arr(n):
            nonlocal ans
            
            if n in memo:
                return memo[n]
            
            if n <= 1:
                ans = max(ans, n)
                return n
             
            if n % 2 == 0:
                res = arr( n // 2)
                ans = max(ans, res)
                memo[n] = res
                return res
            
            else:
                half = n // 2
                
                res = arr(half) + arr(half + 1)
                ans = max(ans, res )
                memo[n] = res

                return res
        
        
        for i in range(n + 1):
            arr(i)
            
        return ans 