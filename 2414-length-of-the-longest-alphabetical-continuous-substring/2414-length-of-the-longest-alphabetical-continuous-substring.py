class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        
        count = 1
        ans = 1
        
        
        for i in range(len(s) - 1):
            
            if (chr(ord(s[i]) + 1)) == s[i + 1] :
                
                count += 1
            else:
                count = 1
                
            ans = max(ans, count)
                
                
                
                
        return ans
        
        
        
        