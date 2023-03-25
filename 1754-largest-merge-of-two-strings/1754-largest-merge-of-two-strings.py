class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        
        w1, w2 = 0, 0
        merge = []
        
        while w1 < len(word1) and w2 < len(word2):
            
            if word1[w1:] >= word2[w2:]:
                merge.append(word1[w1])
                w1 += 1
                    
            else:
                merge.append(word2[w2])
                w2 += 1
                
        merge = ''.join(merge)
        
        merge += word1[w1:] if w1 < len(word1) else ''
        merge += word2[w2:] if w2 < len(word2) else ''
        
        return merge
            
            
        