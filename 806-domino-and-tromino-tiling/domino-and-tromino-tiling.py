class Solution:
    def numTilings(self, n: int) -> int:
        
        @cache
        def dp(n):
            if n == 1:
                return 1
            if n == 2:
                return 2
            if n == 3:
                return 5

            return 2 * dp(n-1) + dp(n - 3)

        return dp(n) % (10**9 + 7)
