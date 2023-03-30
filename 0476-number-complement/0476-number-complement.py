class Solution:
    def findComplement(self, num: int) -> int:
        
        
        ans = 0
        
        for i in range(num.bit_length()):
            
            if not 1 << i & num:
                ans += 1 << i
                
            
        return ans
            
            
            