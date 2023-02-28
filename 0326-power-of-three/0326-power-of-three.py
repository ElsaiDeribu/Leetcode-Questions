class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        if n <= 0: 
            return False
        
        if n < 3 :
            return n == 1
        
        return self.isPowerOfThree(n / 3)
    
        