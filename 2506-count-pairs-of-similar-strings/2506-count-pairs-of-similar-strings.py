class Solution:
    def similarPairs(self, words: List[str]) -> int:
        
        for i in range(len(words)):
            words[i] = set(words[i])
            
        count = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                
                if words[i] == words[j]:
                    count += 1
                    
        return count
                
        