class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        heap = []
        
        
        for i in range(len(heights) - 1):
            
            hDiff = heights[i + 1] - heights[i]
            
            if hDiff > 0:
                
                heappush(heap, hDiff)
                
                if len(heap) > ladders:
                    
                    minimum = heappop(heap)
                    bricks -= minimum
                    
                    if bricks < 0:
                        return i
        
        return len(heights) - 1
                    