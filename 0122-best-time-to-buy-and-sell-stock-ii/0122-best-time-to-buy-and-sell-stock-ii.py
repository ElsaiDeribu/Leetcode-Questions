class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        currMin = prices[0]
        
        for i in range(len(prices)):
            
            if prices[i] > currMin:
                profit += (prices[i] - currMin)
                currMin = prices[i]
            
            else:
                currMin = min(currMin, prices[i])
            
            
        return profit
            
        