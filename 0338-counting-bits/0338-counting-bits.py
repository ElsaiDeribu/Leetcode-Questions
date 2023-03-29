class Solution:
    def countBits(self, n: int) -> List[int]:
        
        def count(n):
            count = 0
            while n:
                
                if n & 1:
                    count += 1
                    
                n >>= 1
                
            return count
        
        ans = []
        for i in range(n + 1):
            ans.append(count(i))
            

        return ans
                
                
                
