class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        ans = 0
        a = 0
        b = 0
        half = len(costs) // 2
        
        costs.sort(key = lambda x : abs(x[0] - x[1]), reverse = True)
        
        for cost in costs:
            if (cost[0] > cost[1] and  b < half) or (a == half and b < half):
                ans += cost[1]
                b += 1
                
            elif a < half or (b == half and a < half):
                ans += cost[0]
                a += 1
                
                
        return ans
                
                
                
                