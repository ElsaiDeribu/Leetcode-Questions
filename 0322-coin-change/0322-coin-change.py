class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        
        @cache
        def coin(remain):
            
            if remain < 0:
                return float("inf")
            
            if remain == 0:
                return 0
            
            res = float("inf")
            for i in range(len(coins)):
                res = min(res, coin(remain -coins[i]))
                
                
            return res + 1
        
        ans = coin(amount)
        
        return -1 if ans == float("inf")  else ans