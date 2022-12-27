class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        
        i = 1
        
        
        while True:
            
            if not i % 2 and not i % n : 
                return i
         
            i += 1