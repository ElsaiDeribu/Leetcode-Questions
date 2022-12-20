class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        ans = ""
        
        i = 0
        j = 0
        n = len(word1) + len(word2)
        
        
        while len(ans) < n:
            if i < len(word1):
                ans += word1[i]
                i += 1
            if j < len(word2):
                ans += word2[j]
                j += 1
                
        return ans
        
        
        
        
        
        
        
        
        
        
        

                
                    