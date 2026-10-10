class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        running_min = float("inf")
        ans = 0

        for price in prices:

            running_min = min(running_min, price)
            profit = price - running_min
            
            ans = max(profit, ans)


        return ans
