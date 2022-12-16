class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        l = 0
        r = len(s) - 1
        
        while l < r:
            if not s[l].isnumeric() and not s[l].isalpha() :
                l += 1
            elif not s[r].isnumeric() and not s[r].isalpha():
                r -= 1
            else:
                if s[l].lower() != s[r].lower():
                    return False
                l += 1
                r -= 1
                
        return True
        
        
        
        