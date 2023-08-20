class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        
        profit = 0
        moneySpent = prices[0]
        
        for price in prices:
            
            profit = max(profit, price - (fee + moneySpent))
            moneySpent = min(moneySpent, price - profit  )
            
        return profit