class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:


        @cache
        def dp(curr):

            if curr >= len(cost):
                return 0

            # take one step
            res1 = dp(curr + 1) 
            # take two steps
            res2 = dp(curr + 2)

            return min(res1, res2) +  cost[curr]


        return min(dp(0), dp(1))

        