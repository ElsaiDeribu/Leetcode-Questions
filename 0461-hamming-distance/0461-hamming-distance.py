class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        
        
        z = x ^ y
        count = 0
        for i in range(z.bit_length()):
            
            if 1 << i & z:
                count += 1
                
                
        return count