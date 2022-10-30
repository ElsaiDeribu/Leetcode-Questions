class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        
        ans = ""
        indices2 = defaultdict(int)
        
        for i in range(len(indices)):
            indices2[indices[i]] = i
           
        i = 0
        
        
        while i < len(s):
            
            if i in indices2 and s[i:i + len(sources[indices2[i]])] == sources[indices2[i]]:
                ans += targets[indices2[i]] 
                i += len(sources[indices2[i]])  
                
            else:
                ans += s[i]
                i += 1
            
        return ans