class Solution:
    def fib(self, n: int) -> int:
        
        @cache
        def helper(n):
            
            if n < 2:
                return n
            
            return helper(n - 1) + helper(n - 2)
        
        
        return helper(n)