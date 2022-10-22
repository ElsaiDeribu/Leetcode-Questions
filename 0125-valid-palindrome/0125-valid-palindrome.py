class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s2 = ""
        nums = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
        for i in range(len(s)):
            
            if ord('a') <= ord(s[i].lower()) <= ord('z') or (s[i] in nums):
                
                s2 += s[i].lower()
                
                
        l = 0
        r = len(s2) - 1
        
        while l < r:
            
            if s2[l] != s2[r]:
                return False
            l += 1
            r -= 1
            
        return True
        
        
        