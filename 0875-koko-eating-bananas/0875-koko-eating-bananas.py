class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        
        def check(speed):
            
            totalHours = 0
            
            for pile in piles:
                time = ceil(pile/speed)
                totalHours += time
                
            return totalHours <= h
        
        
        left = 0
        right = max(piles)
        
        
        while left + 1 < right:
            
            mid = left + (right - left) // 2

            if check(mid):
                right = mid
                
            else:
                left = mid
                
        return right
        