class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        tCount = Counter(t)
        debit = len(tCount)
        minLen = ""
        mx = 10**6
        
        i = j = 0
        
        
        while j < len(s):
            
            while j < len(s) and debit:
                
                if s[j] in tCount:
                    tCount[s[j]] -= 1
                    if tCount[s[j]] == 0:
                        debit -= 1
                
                j += 1
                
            while debit == 0 and i < j:
                if j - i  < mx:
                    mx = j - i 
                    minLen = s[i:j]
                   
                if s[i] in tCount:
                    tCount[s[i]] += 1
                    if tCount[s[i]] > 0:
                        debit += 1
            
                i += 1
            
        return minLen