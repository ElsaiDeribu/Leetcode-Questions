class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        
        
        def recur(n):
            if n == 0:
                return 0
            
            idx = n 
            res = recur(idx // 2)
            
            if res == 0 and idx % 2 != 0:
                return 1
            
            if res == 1 and idx % 2 == 0:
                return 1
                
            return 0
        
        
        return recur(k - 1)
                
            
            
                
        