class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        ans = 0
        running_min = float("inf")

        for price in prices:
            running_min = min(running_min, price)
            profit = price - running_min

            ans = max(ans, profit)

        return ans