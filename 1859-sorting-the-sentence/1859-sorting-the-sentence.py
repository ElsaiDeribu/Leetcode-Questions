class Solution:
    def sortSentence(self, s: str) -> str:
        
        sliced = s.split()
        
        
        for i in range(len(sliced)):
            
            sliced[i] = (int(sliced[i][-1]), sliced[i][:-1])
            
            
        sliced.sort()
        
        for i in range(len(sliced)):
            sliced[i] = sliced[i][1]
            
        
        return " ".join(sliced)
            
        