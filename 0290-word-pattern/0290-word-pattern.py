class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        corr = defaultdict(str)
        s = s.split()
        if len(pattern) != len(s):
            return False
        
        for i in range(len(pattern)):
            if pattern[i] not in corr:
                for j in corr.keys():
                    if corr[j] == s[i]:
                        return False
                corr[pattern[i]] = s[i]
                    
            elif corr[pattern[i]] != s[i]:
                return False
            
        return True
        
        