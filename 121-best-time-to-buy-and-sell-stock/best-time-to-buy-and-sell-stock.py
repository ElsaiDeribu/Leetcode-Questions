class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        running_min = float("inf")
        ans = 0

        for price in prices:

            running_min = min(running_min, price)
            ans = max(price - running_min, ans)


        return ans
