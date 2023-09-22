class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        j = 0
    
        for i in range(len(s)):
            
            while j < len(t) and t[j] != s[i]:
                j += 1                
                
            if j == len(t):
                return False
            
            j += 1
                 
            
        return True
        
        
        
        
     
            
            
        