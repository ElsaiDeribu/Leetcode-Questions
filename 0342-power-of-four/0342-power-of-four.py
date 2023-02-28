class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        if n <= 0:
            return False
        
        def isPow(num):
            
            if num == 1:
                return True
            
            if num < 4:
                return False
            
            return isPow(num / 4)
        
        return isPow(n)