class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        ans = []
        comb = []
        
        def recur(i):
            
            if len(comb) == k:
                ans.append(comb[:])
                return
            
            if i > n:
                return 
            
            comb.append(i)
            recur(i + 1)
            comb.pop()
            recur( i + 1)
            
            
#             for i in range(start, n + 1):
                
#                 comb.append(i)
#                 recur(i + 1)
#                 comb.pop()
                    
        recur(1)
        
        return ans
                
            
            
 