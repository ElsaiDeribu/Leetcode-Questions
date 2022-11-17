class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maxVol = 0
        
        while l < r:
            currVol = min(height[l], height[r]) * (r - l)
            maxVol = max(maxVol, currVol)
            
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
                
        return maxVol
                
            
            
        