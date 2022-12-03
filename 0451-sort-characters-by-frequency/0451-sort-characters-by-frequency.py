class Solution:
    def frequencySort(self, s: str) -> str:
        
        count = Counter(s)
        count = sorted(count.items(), key = lambda x: x[1], reverse = True)
        ans = ""
        for i in range(len(count)):
            ans += count[i][0] * count[i][1]
            
        return ans
        
        