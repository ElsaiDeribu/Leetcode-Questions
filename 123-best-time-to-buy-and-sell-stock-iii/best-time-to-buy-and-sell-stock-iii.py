class Solution:
    def maxProfit(self, prices: List[int]) -> int:

         
        @cache
        def dp(i, buy, t):
            if i == len(prices) or not t:
                return 0

            if buy:
                return max(-prices[i] + dp(i + 1, 0, t), dp(i + 1, 1, t))
            else:
                return max(prices[i] + dp(i + 1, 1, t - 1), dp(i + 1, 0, t))

        return dp(0,1, 2)


        