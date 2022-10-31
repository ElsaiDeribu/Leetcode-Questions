class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        debit = Counter(t)
        count = len(debit)
        mn = 10**6
        ans = ""
        
        i = j = 0
        
        
        while j < len(s):
            
            while j < len(s) and count:
                if s[j] in debit:
                    debit[s[j]] -= 1
                    if debit[s[j]] == 0:
                        count -= 1
                        
                j += 1
                
            while i < j and count == 0:
                if j - i < mn:
                    mn = j - i
                    ans = s[i:j]
                    
                if s[i] in debit:
                    debit[s[i]] += 1
                    if debit[s[i]] > 0:
                        count += 1
                        
                i += 1
          
        
        return ans