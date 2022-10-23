class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        l = 0
        r = len(cardPoints) - (k + 1)
        ans = 0
        total = sum(cardPoints)
        subarrSum = 0
        
        if r < 0:
            return total
        
        for i in range(r + 1):
            subarrSum += cardPoints[i]

        while r < len(cardPoints):
            
            ans = max(ans, total- subarrSum)
            
            subarrSum -= cardPoints[l]
            l += 1
            r += 1
            if r < len(cardPoints):
                subarrSum += cardPoints[r]
            
                
        return ans
            
            
            
        
        
        
        
        
 
        