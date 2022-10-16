class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
           
        count = Counter(p)
        subarr = defaultdict(int)
        ans = []
        
        if len(p) > len(s):
            return []
        
        for i in range(len(p)):
            subarr[s[i]] += 1
            j = i
        
        
        k = 0
        
        while j < len(s):

            if subarr == count:
                ans.append(k)
                
            subarr[s[k]] -= 1
            if subarr[s[k]] == 0:
                subarr.pop(s[k])
            k += 1
            j +=1
            if j < len(s):
                subarr[s[j]] += 1

        return ans
            
        
        
        
                
            

        
        
            
            
        
        
        