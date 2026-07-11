class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        
        longestSub = 0
        
        def findLongestFor(letter, conv):
            
            longest = 0
            left = 0
            for right in range(len(s)):
                if s[right] != letter:
                    conv -= 1
                
                while conv < 0:
                    if s[left] != letter:
                        conv += 1
                        
                    left += 1
                    
                longest = max(longest, right - left + 1)
                
            return longest
        
        for i in range(ord('A') , ord('Z') + 1):
            currentChar = chr(i)
            longestSub = max(longestSub, findLongestFor(currentChar, k))
        
        return longestSub  
                
        