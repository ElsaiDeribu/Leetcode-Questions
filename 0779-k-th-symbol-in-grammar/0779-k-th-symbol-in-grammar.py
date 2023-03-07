class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        
        indx = k - 1
        
        
        def helper(index):
            
            if index == 0: 
                return 0
            
            if index % 2 == 0 :
                return helper(index // 2)
            
            else: 
                temp = helper(index // 2)
                
                if temp == 1:
                    return 0
                
                else:
                    return 1
                
            
        return helper(indx)
            
            