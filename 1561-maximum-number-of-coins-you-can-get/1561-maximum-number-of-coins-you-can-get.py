class Solution:
    def maxCoins(self, piles) -> int:
        
        piles.sort()
        triplets = []
        l = 0
        r = len(piles) - 1
        ans = 0
        
        while l < r:
            
            tri = []
            
            tri.append(piles[l])
            tri.append(piles[r])
            r -= 1
            tri.append(piles[r])
            
            triplets.append(tri)
            r -= 1
            l += 1
            
            
        for i in triplets:
            ans += i[2]
        
        return ans
       