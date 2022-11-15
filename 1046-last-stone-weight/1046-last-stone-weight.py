class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heap = []
        
        for i in stones:
            heappush(heap, -i)
        
        while len(heap) > 1:
            
            y = -heappop(heap)
            x = -heappop(heap)
            
            heappush(heap, -(y - x))
            
        
        return -heap[0]
        