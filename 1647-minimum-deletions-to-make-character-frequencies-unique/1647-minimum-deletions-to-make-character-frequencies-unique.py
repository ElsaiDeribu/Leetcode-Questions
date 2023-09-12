class Solution:
    def minDeletions(self, s: str) -> int:
        
        count = [[key, val] for key, val in Counter(s).items()]
        count.sort(key = lambda x: x[1], reverse =True)
        ans = 0
        
        for i in range(1, len(count)):
            if count[i - 1][1] == count[i][1]:
                count[i][1] -= 1 
                ans += 1
                
            elif count[i - 1][1] == 0:
                ans += count[i][1]
                count[i][1] = 0  
                
            elif count[i - 1][1] < count[i][1]:
                ans += count[i][1] - count[i - 1][1] + 1
                count[i][1] = count[i - 1][1] - 1 
                
        return ans
        
         