class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        
        windowElements = defaultdict(int)
        count = 0
        l = 0
        r = 0
        
        if len(s) < 3:
            return count
        
        for i in range(3):
            windowElements[s[i]] += 1
            r = i
            
        if len(windowElements) == 3:
            count += 1
            
            
        while r < len(s):
            
            windowElements[s[l]] -= 1
            if windowElements[s[l]] == 0:
                windowElements.pop(s[l])
            l += 1
            
            r += 1
            if r < len(s):
                windowElements[s[r]] += 1
                if len(windowElements) == 3:
                    count += 1

                    
        return count
            
        