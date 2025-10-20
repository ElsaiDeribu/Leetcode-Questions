class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        # Base case: after the last day, no profit possible
        future_profit_if_free = 0      # same as dp[i+1][can_buy=True]
        future_profit_if_holding = 0   # same as dp[i+1][can_buy=False]

        # Iterate backwards through days
        for i in range(n - 1, -1, -1):
            # If I'm free (can buy today), I can:
            # - Buy now (-prices[i]) and then be holding (next state)
            # - Skip today and remain free
            best_profit_if_buy_today = max(
                -prices[i] + future_profit_if_holding,  # buy
                future_profit_if_free                    # skip
            )

            # If I'm holding a stock, I can:
            # - Sell now (+prices[i]) and become free
            # - Skip selling today and keep holding
            best_profit_if_sell_today = max(
                prices[i] + future_profit_if_free,       # sell
                future_profit_if_holding                 # skip
            )

            # Update for next iteration
            future_profit_if_free = best_profit_if_buy_today
            future_profit_if_holding = best_profit_if_sell_today

        # Initially, we are free (no stock held)
        return future_profit_if_free
