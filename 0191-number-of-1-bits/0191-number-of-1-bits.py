class Solution:
    def hammingWeight(self, n: int) -> int:
        
        count = 0
        for i in range(n.bit_length()):
            
            if 1 << i & n:
                count += 1
                
        return count