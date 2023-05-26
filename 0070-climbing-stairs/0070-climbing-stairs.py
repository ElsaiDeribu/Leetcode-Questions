class Solution:
    def climbStairs(self, n: int) -> int:
        
        
        @lru_cache
        def recur(step):
            
            if step == 0:
                return 1
            
            if step == -1:
                return 0
            
            p1 = step - 1  
            p2 = step - 2 
            
            res1 = recur(p1)
            res2 = recur(p2)
            
            total =  res1 + res2 
            
            return total 
        
        
        return recur(n)