class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        
        
        closest = [0] * len(s)
        
        req = None
        
        for i in range(len(s)):
            
            if s[i] == c:
                closest[i] = "c"
                req = i
                
            elif req != None:
                closest[i] = i - req
                
        req = None        
        for i in range(len(s) - 1, -1 , -1):
            if s[i] == c:
                closest[i] = 0
                req = i
                
            elif req != None and closest[i] != 0:
                
                closest[i] = min(closest[i],req - i )
            
            elif req != None:
                closest[i] = req - i
        
            
        return closest