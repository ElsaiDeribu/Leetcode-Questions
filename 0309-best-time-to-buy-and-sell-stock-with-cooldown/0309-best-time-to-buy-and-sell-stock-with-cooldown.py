class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        
        @lru_cache(None)
        def find(idx, prev):
            if idx >= len(prices):
                return 0
            
            if prev == False:
                buy = find(idx + 1, True) - prices[idx]
                notBuy = find(idx + 1, False)
                return max(buy, notBuy)
            
            else:
                sell = find(idx + 2, False) + prices[idx]
                notSell = find(idx + 1, True) 
                return max(sell, notSell)
            
            
        return find(0, False)
        