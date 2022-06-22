class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        
        for i in stones:
            heappush(heap, -i)
            
        while heap:
            if len(heap) == 1:
                 break
            y = -heappop(heap)
            x = -heappop(heap)
            if x == y :
                continue
            y = y - x
            heappush(heap, -y)
            
         
                
        return -heap[0] if heap else 0
            
            
            
            