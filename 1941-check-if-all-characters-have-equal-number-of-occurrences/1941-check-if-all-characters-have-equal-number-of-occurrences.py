class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        
        count= Counter(s)
        std = count[s[0]]
        
        for i in count:
            if count[i] != std:
                return False
            
        return True
        
        