class Solution:
    def mySqrt(self, x: int) -> int:
        
        left = 0
        right = x + 1
        
        while left + 1 < right:
            
            mid = left + ((right - left) //2)
            res = mid * mid
            
            if res <= x:
                left = mid 
                
            else:
                right = mid 
            
            
        return left