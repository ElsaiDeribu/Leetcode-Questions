class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        kthSmallest = 0
        
        for i in matrix:
            for j in i:
                heappush(heap, j)
                
        while k :
            kthSmallest = heappop(heap)
            k -= 1
            
        return kthSmallest