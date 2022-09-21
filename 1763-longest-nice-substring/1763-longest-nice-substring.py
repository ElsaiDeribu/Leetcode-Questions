class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        
        longest = ""
        
        def isGood(string):
            
            chars = set(string)
            for c in string:
                if c.upper() not in chars or c.lower() not in chars:
                    return False
                
            return True
            
            
           
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                
                if isGood(s[i:j]) and len(s[i:j]) > len(longest):
                    longest = s[i:j]
                
        return longest
        
            
            
            
            
        
        
        
        