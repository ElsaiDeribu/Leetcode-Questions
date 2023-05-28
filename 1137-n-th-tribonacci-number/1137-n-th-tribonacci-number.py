class Solution:
    def tribonacci(self, n: int) -> int:
        
        memo = {}
        
        def trib(n):
            
            if n in memo:
                return memo[n]
            
            if n == 2:
                return 1
            
            if n <= 1:
                return n
            
            res =  trib(n - 1) + trib(n - 2) + trib(n - 3)
            memo[n] = res
            
            return res
            
        return trib(n)