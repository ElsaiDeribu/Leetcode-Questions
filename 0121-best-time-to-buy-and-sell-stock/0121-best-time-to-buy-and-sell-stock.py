class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        currMin = prices[0]
        
        for i in range(len(prices)):
            
            currMin =  min(currMin ,prices[i])
            profit = max(profit, (prices[i] - currMin))            

        return profit