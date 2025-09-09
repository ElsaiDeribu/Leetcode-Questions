class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        @cache
        def dp(r, c):
            if r == m - 1 and c == n - 1:
                return 1

            if r >= m or c >= n:
                return 0

            # move left
            left = dp(r, c + 1)

            # move down
            down = dp(r + 1, c)

            return left + down


        return dp(0,0)
