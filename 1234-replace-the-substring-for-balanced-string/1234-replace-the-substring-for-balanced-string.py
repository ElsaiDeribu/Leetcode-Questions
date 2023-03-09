class Solution:
    def balancedString(self, s: str) -> int:
        
        count = Counter(s)
        share = len(s)// 4
        windowElements = defaultdict(int)
        minSize = len(s)
        left = 0

        for item in ["Q", "W", "E", "R"]:
            count[item] -= share
            if count[item] <= 0:
                del count[item]
            
        if not count:
            return 0
        
        
        def check():
            for item in count:
                if item not in windowElements or windowElements[item] < count[item]:
                    return False
                
            return True
            
            
        for right in range(len(s)):
            
            windowElements[s[right]] += 1
            
            while check():
                
                minSize = min(minSize, right - left + 1)
                
                windowElements[s[left]] -= 1
                if windowElements[s[left]] == 0:
                    del windowElements[s[left]]
                    
                left += 1
                
        return minSize 
                
                
            
            
            
            
            