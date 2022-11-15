class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        heap = []
        ans = 0
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                heappush(heap, matrix[i][j])
                
        while k:
            ans = heappop(heap)
            k-= 1
        
        return ans
        
        
#         # Sorting solution
#         elements = []
#         for i in matrix:
#             elements.extend(i)
                
#         elements.sort()
#         return elements[k - 1]
