class Solution:
    def bitwiseComplement(self, n: int) -> int:
        
        
        ans = 0
        if n == 0 : return 1
        for i in range(n.bit_length()):
            
            if 1 << i & n == 0:
                ans += 2**i 
                
        return ans