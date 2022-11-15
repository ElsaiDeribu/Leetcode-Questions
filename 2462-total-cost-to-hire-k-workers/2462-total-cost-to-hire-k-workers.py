class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        
        heap = []
        r = len(costs) - 1
        l = 0
        ans = 0
        
        while l < candidates and l <= r:
            heappush(heap, (costs[l], l))
            if r != l:
                heappush(heap, (costs[r], r))
            l += 1
            r -= 1
        
        while k :
            c = heappop(heap)
            ans += c[0] 
            
            if c[1] < l and l <= r:
                heappush(heap, (costs[l], l))
                l += 1
            elif l <= r:
                heappush(heap, (costs[r], r))
                r -= 1
        
            k -= 1
            
        return ans
        
        
                
                     
                     

                
                
                
                
                
        
        
        
            
            
        