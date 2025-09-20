class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        
        heap = []
        l, r = 0, len(costs) - 1
        ans = 0
        
        for _ in range(candidates):
            if l <= r: heappush(heap, (costs[l], l)); l += 1
            if l <= r: heappush(heap, (costs[r], r)); r -= 1


        while k :
            val, idx = heappop(heap)
            ans += val
            
            if l <= r:
                if idx < l:
                    heappush(heap, (costs[l], l))
                    l += 1
                else:
                    heappush(heap, (costs[r], r))
                    r -= 1
        
            k -= 1
            
        return ans
        
        
                
                     
                     

                
                
                
                
                
        
        
        
            
            
        