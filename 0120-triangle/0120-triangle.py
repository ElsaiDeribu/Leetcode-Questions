class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        
        def isInbound(index):
            row = index[0]
            col = index[1]
            
            return 0 <= row < len(triangle) and 0 <= col < len(triangle[row])
        
        @cache
        def dp(index):
            
            row = index[0]
            col = index[1]
            
            if not isInbound((row + 1, col)) and not isInbound((row + 1, col + 1)):
                return triangle[index[0]][index[1]]
            
            left = float("inf")
            right = float("inf")
            
            if isInbound((row + 1, col)): 
                left = dp((row + 1, col))
                
            if isInbound((row + 1, col + 1)) : 
                right = dp((row + 1, col + 1))
            
            
            
            return min(left, right) + triangle[index[0]][index[1]]
            
             
            
        return dp((0,0))    
            