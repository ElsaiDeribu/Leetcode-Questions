class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        temp = words[:]
    
    
        def isOrdered(w1, w2):
            n = min(len(w1), len(w2))
            for i in range(n):
                if order.index(w1[i]) > order.index(w2[i]):
                    return False
                
                elif order.index(w1[i]) < order.index(w2[i]):
                    return True
            if len(w1) < len(w2):
                return True
                
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if not isOrdered(words[i], words[j]):
                    words[i], words[j] = words[j], words[i]

                    
        return temp == words
            