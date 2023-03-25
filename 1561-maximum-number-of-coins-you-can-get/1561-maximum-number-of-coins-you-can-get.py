class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        
        piles.sort()
        
        alice = len(piles) - 1
        me = alice - 1
        bob = 0
        myPile = 0
        
        while bob < me:
            
            myPile += piles[me]
            bob += 1
            me -= 2
            
        return myPile
            
        