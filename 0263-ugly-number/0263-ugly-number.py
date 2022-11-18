class Solution:
    def isUgly(self, n: int) -> bool:
        
        
        while n > 1:
            temp = n
            if n % 2 == 0:
                n /= 2
            if n % 3 == 0:
                n /= 3
            if n % 5 == 0:
                n /= 5
                
            if temp == n:
                return False
            
        return True if n == 1 else False
            
        