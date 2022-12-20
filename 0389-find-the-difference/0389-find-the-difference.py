class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        s = sorted(s)
        t = sorted(t)
        
        n = max(len(t), len(s))
        
        for i in range(n):
            
            if i < len(s) and i < len(t):
                if s[i] != t[i]:
                    return t[i]
        
        return t[i] 