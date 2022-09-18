class Solution:
    def frequencySort(self, s: str) -> str:
        
        count = Counter(s)
        ans = ''
        
        sortedDictionary = {k:v for k, v in sorted(count.items(), key = lambda v: v[1], reverse = True)}
        
        for i in sortedDictionary:
            ans += i * sortedDictionary[i]
            
        return ans
            
        