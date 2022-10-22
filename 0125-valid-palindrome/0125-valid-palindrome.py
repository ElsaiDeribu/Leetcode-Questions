class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s2 = ""
        
        for i in range(len(s)):
            
            if ord('a') <= ord(s[i].lower()) <= ord('z') or ( ord('0') <= ord(s[i]) <= ord('9')):
                s2 += s[i].lower()
                
                
        l = 0
        r = len(s2) - 1
        
        while l < r:
            
            if s2[l] != s2[r]:
                return False
            l += 1
            r -= 1
            
        return True

        
        
        