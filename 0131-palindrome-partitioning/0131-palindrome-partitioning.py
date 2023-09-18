class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        @cache
        def dp(start):
            if start >= len(s):
                return []
            
            ans = []
            for i in range(start, len(s)):
                curr = s[start:i + 1] 
                pal = curr == curr[::-1]
                temp = [curr]
                
                if pal:
                    res = dp(i + 1)
                    for p in res:
                        temp.extend(p) 
                        ans.append(temp[:])
                        temp = [curr]
                    if not res:
                        ans.append(temp)

            return ans     
        
        return dp(0)
                        
                        
                        
                        
                        
                        