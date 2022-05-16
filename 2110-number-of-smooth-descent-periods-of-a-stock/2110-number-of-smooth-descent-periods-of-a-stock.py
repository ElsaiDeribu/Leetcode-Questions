class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        ans = [1]
        
        for i in range(len(prices)-1):
            if prices[i] == prices[i+1] + 1:
                ans.append(ans[-1] + 1)
            else:
                ans.append(1)
                
        return sum(ans)