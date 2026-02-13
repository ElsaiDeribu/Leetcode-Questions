class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0
        curr_min = float("inf")

        for price in prices:

            curr_min = min(curr_min, price)
            max_profit = max(price - curr_min, max_profit)

        return max_profit