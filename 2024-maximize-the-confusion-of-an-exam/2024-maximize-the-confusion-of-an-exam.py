class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        
        
        intruder = 0
        longest = 0
        l = 0
        r = 0
        t = k
        

        while l < len(answerKey):
            
            while r < len(answerKey) and (intruder < k or answerKey[r] == 'T'):
                if answerKey[r] != 'T':
                    intruder += 1
                    
                r += 1
            
            longest =  max(longest, r - l ) 
            
            if answerKey[l] != 'T':
                intruder -= 1
        
            l += 1
            
            
        intruder = 0
        l = 0
        r = 0
        while l < len(answerKey):
            
            while r < len(answerKey) and (intruder < k or answerKey[r] == 'F'):
                if answerKey[r] != 'F':
                    intruder += 1
                    
                r += 1
            
            longest =  max(longest, r - l ) 
            
            if answerKey[l] != 'F':
                intruder -= 1
                
            l += 1
            
            
        return longest