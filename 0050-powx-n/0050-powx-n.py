class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        
        
#         def findPower(number, power, curr):
            
#             if power == 1:
#                 return number
#             if power == -1:
#                 return 
            
#             curr = 
#             return 
        
        
        
        
        
        
        
        
        
        
        # DP solution
        

        @cache
        def findPower(number, power):
            
            
            if power == 1:
                return number
            
            if power == 0:
                return 1
            
            if power == -1:
                return 1 / number
   
            if  power % 2 == 0:
                left = right = power / 2
                
            else:
                left, right = power // 2, (power // 2) + 1
                
            result = findPower(number, left) * findPower(number, right)
            
            return result
                
          
        return findPower(x, n)