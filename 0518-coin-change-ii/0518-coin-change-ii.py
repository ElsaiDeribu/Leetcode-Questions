class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        coins.sort()
        
        @cache
        def coin(remain, idx):
            
            if remain < 0 or idx >= len(coins):
                return 0
            
            if remain == 0:
                return 1
            
            return coin(remain - coins[idx], idx) + coin(remain, idx + 1)
            
            
        return coin(amount, 0)
        
        
        
    