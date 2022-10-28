class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        
        if len(changed) % 2:
            return []
        
        changed.sort()
        ans = []
        count = Counter(changed)
        
        
        for i in range(len(changed) ):
            
            if changed[i] == 0 and count[0] >= 2:
                ans.append(0)
                count[0] -= 2
            
            if changed[i] > 0 and (count[changed[i]] > 0) and (count[2 * changed[i]] > 0 ):
                ans.append(changed[i])
                count[changed[i]] -= 1
                count[2 * changed[i]] -= 1
                
        
        return ans if len(ans) == len(changed) // 2 else []