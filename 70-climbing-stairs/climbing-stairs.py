class Solution:
    def climbStairs(self, n: int) -> int:
        
        dic = {}

        def dp(curr):
            if curr in dic:
                return dic[curr]

            if curr >= n:
                return 1 if curr == n else 0

            dic[curr] = dp(curr + 2) + dp(curr + 1)
            
            return dic[curr]

        return dp(0)