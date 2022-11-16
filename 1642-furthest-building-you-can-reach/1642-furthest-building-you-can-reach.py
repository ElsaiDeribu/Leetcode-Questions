class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        heap = []
        
        for i in range(len(heights)):
            if i == len(heights) - 1:
                break
            hDiff = heights[i + 1] - heights[i]
            if ladders and hDiff > 0:
                heappush(heap, hDiff)
                if len(heap) > ladders:
                    bricksRequired = heappop(heap)
                    if bricksRequired > bricks:
                        break
                    bricks -= bricksRequired
            elif hDiff > 0:
                if hDiff > bricks:
                    break
                bricks -= hDiff
                
        return i
            

            
        