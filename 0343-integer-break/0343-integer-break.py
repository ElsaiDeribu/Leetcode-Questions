class Solution:
    def integerBreak(self, n: int) -> int:
        
        
        if n <= 3:
            return n - 1
        
        rem = n % 3
        temp = (n // 3)
        
        if rem == 0:
            return 3 ** temp
        
        if rem == 1:
            return (3 ** (temp - 1)) * 4
        
        
        return (3 ** temp) * 2
        
                