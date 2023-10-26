class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        
        arr = set(arr)
        
        @cache
        def dp(parent):
            
            res = 1
            for element in arr:

                child1 = element
                child2= parent / element

                if child2 in arr:
                      res += dp(child1) * dp(child2)

            return res    
      
  
            
        ans = 0
        for num in arr:
            ans +=  dp(num)
            ans %= (10**9 + 7)
             
        return ans
    
    
    
    
    
    