class Solution:
    def numTrees(self, n: int) -> int:
        
        @cache
        def count(length):
            if length == 1 or length == 0:
                return 1
            
            res = 0
            for i in range(length ):
                left = count(i)
                right = count(length - i - 1)
                
                res += (left * right)
                
            return res
        
        
        return count(n)