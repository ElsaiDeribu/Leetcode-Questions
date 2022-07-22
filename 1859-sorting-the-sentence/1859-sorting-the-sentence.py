class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        sortedWords = []
        for i in words:
            sortedWords.append((i[-1], i[:-1]))
        sortedWords.sort()
        for i in range(len(words)):
            words[i] = sortedWords[i][1]
            
        return (' '.join(words))
        
        
            
        

            
            
            
            