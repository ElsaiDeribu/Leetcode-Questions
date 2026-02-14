class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        
        profit = 0
        curr = prices[0]

        for price in prices:

            if price > curr:
                profit += price - curr
                curr = price

            else:
                curr = min(curr, price)


        return profit