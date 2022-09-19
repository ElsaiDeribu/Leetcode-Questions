class Solution:
    def isHappy(self, n: int) -> bool:
        
        visited = set()
        
        temp = n
        total = 0
        
        while True:
            
            temp = str(temp)
            
            for i in temp:
                total +=(int(i)**2)
                
            if total in visited:
                return False
            
            visited.add(total)
            
            if total == 1:
                return True
            
            temp = total
            total  = 0
            
            
                
            
            
        