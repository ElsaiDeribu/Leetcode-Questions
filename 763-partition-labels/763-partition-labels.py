class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        count = Counter(s)
        visited = set()
        ans = []
        
        i = 0
        j = 0
        
  
        while j < len(s):
        
            i = j
            visited.add(s[i])

            while j < len(s) and len(visited) > 0:
                
                if s[j] in visited:
                    count[s[j]] -= 1
                    if count[s[j]] == 0:
                        visited.remove(s[j])
                    j += 1
                else:
                    visited.add(s[j])
                    count[s[j]] -= 1
                    if count[s[j]] == 0:
                        visited.remove(s[j])
                    j += 1
                    
            ans.append(j - i)
            
                    
                
        return ans
                    
                

            
        
        