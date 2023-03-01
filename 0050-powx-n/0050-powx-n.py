class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        memo = defaultdict(int)
        
        def findPower(number, power):
            
            if power in memo:
                return memo[power]
            
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
            
            memo[power] = result
            
            return result
                
          
        return findPower(x, n)