class Solution:
    def sortSentence(self, s: str) -> str:
        
        s = s.split()
        
        for i in range(len(s)): 
            s[i] = (s[i][-1], s[i][:-1])
            
        s.sort()
        
        for i in range(len(s)): 
            s[i] = s[i][1]
        
        return ' '.join(s)
        
            
            
        
          
