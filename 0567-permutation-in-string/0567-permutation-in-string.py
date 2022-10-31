class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        count1 = Counter(s1)
        
        i = 0
        j = len(s1) - 1
        
        windowEl = Counter(s2[i:j+1])
        
        if count1 == windowEl:
            return True
        
        
        while j < len(s2):
            
            j += 1
            if j < len(s2):
                windowEl[s2[j]] += 1
            
            
            windowEl[s2[i]] -= 1
            
            if windowEl[s2[i]] == 0:
                windowEl.pop(s2[i])
                
            i += 1
            
            if windowEl == count1:
                return True
            
        return False
            
            