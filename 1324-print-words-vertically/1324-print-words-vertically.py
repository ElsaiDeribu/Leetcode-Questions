class Solution:
    def printVertically(self, s: str) -> List[str]:
        
    
        s = s.split()
        colLen = 0
        
        for row in s:
            colLen = max(colLen, len(row))
        
        
        ans = [[' ']* len(s) for i in range(colLen)]
        
        
        for i in range(len(s)):
            for j in range(colLen):
                if j < len(s[i]):
                    ans[j][i] = s[i][j]
        
        for i in range(len(ans)):
            
            ans[i] = ''.join(ans[i]).rstrip()
            
            
        return ans
            
