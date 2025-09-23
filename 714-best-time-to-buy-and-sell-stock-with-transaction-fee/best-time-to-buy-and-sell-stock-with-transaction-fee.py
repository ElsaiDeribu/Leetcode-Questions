class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:

        @cache
        def dp(i, buy):
            if i == len(prices):
                return 0

            if buy:
                profit1 = -prices[i] + dp(i + 1, 0)
                profit2 = dp(i + 1, 1)
                return max(profit1,profit2)

            else:
                profit3 = prices[i] + dp(i + 1, 1) - fee
                profit4 = dp(i + 1, 0)

                return max(profit3,profit4)

            
        return dp(0, 1)
        