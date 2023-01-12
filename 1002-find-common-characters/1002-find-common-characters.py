class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        
        
        arrayDict = [float("inf")] * 26
        
        
        
        for i in range(len(words)):
            localArrayDict = [0] * 26
            for j in range(len(words[i])):
                
                currLetter = words[i][j]
                
                localArrayDict[ord(currLetter) - 97] += 1
                
            for k in range(len(localArrayDict)):
                arrayDict[k] = min(arrayDict[k],localArrayDict[k] )
                
                
        commonLetters = []
        
        for i in range(len(arrayDict)):
                for j in range(arrayDict[i]):
                    commonLetters.append(chr(i + 97)) 
            
            
            
        return commonLetters