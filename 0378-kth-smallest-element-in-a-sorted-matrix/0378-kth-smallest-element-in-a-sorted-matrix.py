class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        heap = []
        
        for i in range(len(matrix)):
            heappush(heap, (matrix[i][0], (i, 0)))
            
            
        while k:
            smallest = heappop(heap)[1]
            
            row = smallest[0]
            col = smallest[1]
            nxt = col + 1
            
            if nxt < len(matrix[0]):
                heappush(heap, (matrix[row][nxt], (row, nxt)))
            
            k -= 1
            
        return matrix[smallest[0]][smallest[1]]
            
            
        