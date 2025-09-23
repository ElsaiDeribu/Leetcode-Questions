class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       
        @cache
        def dp(i, buy):
            if i == len(prices):
                return 0

            if buy:
                return max(-prices[i] + dp(i + 1, 0), dp(i + 1, 1))
            else:
                return max(prices[i] + dp(i + 1, 1), dp(i + 1, 0))

        return dp(0,1)


        