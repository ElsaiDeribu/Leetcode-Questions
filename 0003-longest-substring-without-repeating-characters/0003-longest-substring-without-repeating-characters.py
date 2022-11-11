class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        windowElements = set()
        l, r = 0, 0
        maxLen = 0
        
        while r < len(s):
            while s[r] in windowElements:
                windowElements.remove(s[l])
                l += 1
            
            windowElements.add(s[r])
            maxLen = max(maxLen, r - l + 1)
            
            r += 1
        
        return maxLen