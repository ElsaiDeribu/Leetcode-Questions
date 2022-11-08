class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        merged = []
        
        i = 0
        j = 0
        
        while len(merged) < (len(word1) + len(word2)):
                
                if i < len(word1):
                    merged.append(word1[i])
                    i += 1
                
                if j < len(word2):
                    merged.append(word2[j])
                    j += 1
                
                
        return ''.join(merged)
                
                    