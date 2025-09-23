class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        smallest = float("inf")
        profit = 0

        for n in prices:
            smallest = min(smallest, n)
            profit = max(profit, n - smallest)

        return profit
      