class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        
        def isInbound(index):
            row = index[0]
            col = index[1]
            return 0 <= row < len(matrix) and 0 <= col < len(matrix[0])
        
        
        @cache
        def fall(index):
            
            if isInbound(index) and index[0] == len(matrix) - 1:
                return matrix[index[0]][index[1]]
              
            p1 = fall((index[0] + 1, index[1] - 1)) if isInbound((index[0] + 1, index[1] - 1)) else float("inf")
            p2 = fall((index[0] + 1, index[1] + 1)) if isInbound((index[0] + 1, index[1] + 1)) else float("inf")
            p3 = fall((index[0] + 1, index[1]))
            
            return min(p1, p2, p3) + matrix[index[0]][index[1]]
                
        ans = float("inf")
        for col in range(len(matrix[0])):
            ans = min(ans, fall((0, col)))
            
        return ans