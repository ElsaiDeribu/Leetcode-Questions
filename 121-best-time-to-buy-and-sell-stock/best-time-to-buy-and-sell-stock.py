class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0
        running_min = float("inf")

        for price in prices:
            running_min = min(running_min, price)
            max_profit = max(max_profit, price - running_min)

        return max_profit