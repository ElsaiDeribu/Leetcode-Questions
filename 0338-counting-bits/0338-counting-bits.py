class Solution:
    def countBits(self, n: int) -> List[int]:
        
        def count(num):
            res = 0
            for i in range(num.bit_length()):
                if (1 << i) & num:
                    res += 1      
            return res
        
        
        
        ans = []
        for i in range(n + 1):
            ans.append(count(i))
            
        return ans