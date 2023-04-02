class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        
        
        prev = n & 1
        
        for i in range(1, n.bit_length()):
            
            currBit = 1 << i & n
            currBit = 0 if currBit == 0 else 1 
            
            if currBit == prev:
                return False
            
            else:
                prev = currBit
                
                
        return True
            
            