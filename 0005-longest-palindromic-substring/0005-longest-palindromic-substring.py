class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        
        def check(l, r):
            
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                
            return l, r
        
        
        longest = 0
        limit = [1,1]
        
        
        for i in range(len(s)):
            
            even = check(i, i)
            odd = check(i, i + 1)
            
            if even[1] - even[0] + 1 > longest:
                limit = [even[0], even[1]]
                longest = even[1] - even[0] + 1
            
            if odd[1] - odd[0] + 1 > longest:
                limit = [odd[0], odd[1]]
                longest = odd[1] - odd[0] + 1
                
        return s[limit[0] + 1 : limit[1]]
                
            
            
            
            
        
        