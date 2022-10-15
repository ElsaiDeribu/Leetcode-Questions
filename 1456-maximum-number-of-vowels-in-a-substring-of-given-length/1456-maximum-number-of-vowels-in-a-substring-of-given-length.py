class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        vouls = ['a', 'e', 'i', 'o', 'u']
        vouls = set(vouls)
        
        count = 0
        ans = 0
        
        l = 0
        r = 0
        
        for i in range(k):

            if s[i] in vouls:
                count += 1
            r = i
            
        ans = count
        
        while r < len(s):
            
            r += 1
            
            if r < len(s) and s[r] in vouls:
                count += 1
                
            if s[l] in vouls:
                count -= 1
                
            l += 1
            
            ans = max(ans, count)
            
            
        return ans
                
        