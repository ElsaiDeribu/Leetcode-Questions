class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        
        costs = sorted(costs, key = lambda x: abs(x[0] - x[1]), reverse = True)
        a = 0
        b = 0
        half = len(costs) // 2
        ans = 0
        
        for i in range(len(costs)):
            costA = costs[i][0]
            costB = costs[i][1]
            
            if costA < costB and a < half or b == half:
                a += 1
                ans += costA
                
            else:
                b += 1
                ans += costB
                
                
        return ans