class Solution:
    def checkValidString(self, s: str) -> bool:
        
        stars = []
        opening = []
        
        
        for i in range(len(s)):
            
            if s[i] == '(':
                opening.append(i)
                
            elif s[i] == '*':
                stars.append(i)
                
            if s[i] == ')':
                
                if opening:
                    opening.pop()
                    
                elif stars:
                    stars.pop()
                
                else:
                    return False
                    
                    
        if opening:
            
            for i in range(len(opening) - 1, -1, -1):
                
                if stars and opening[i] < stars[-1]:
                    stars.pop()
                    
                else:
                    return False
                
                
        return True
                
                
                
            
        
        
        

                 
                