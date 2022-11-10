class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        
        maxTLen, maxFLen, l, r = 0, 0, 0, 0
        conv = k
        
        while r < len(answerKey):
            if answerKey[r] == 'F':
                conv -= 1
                    
            while conv < 0:
                if answerKey[l] == 'F':
                    conv += 1
                l += 1
            
            r += 1
            maxTLen = max(maxTLen, r - l )

            
            
        conv = k            
        l, r = 0, 0    
        while r < len(answerKey):
            if answerKey[r] == 'T':
                conv -= 1
                    
            while conv < 0:
                if answerKey[l] == 'T':
                    conv += 1
                l += 1
            
            r += 1      
            maxFLen = max(maxFLen, r - l )

            
            
        return max(maxTLen, maxFLen)