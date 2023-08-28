class Solution:
    def knightProbability(self, n: int, k: int, r: int, c: int) -> float:
        
        
        if k == 0:
            return 1
        
        directions = [(-1,-2),(-2,-1),(-2,1),(-1,2),(1,-2),(2,-1),(2,1),(1,2)]
        
        def isInbound(index):
            row, col = index
            return 0 <= row < n and 0 <= col < n
        
        @cache    
        def explore(index, moves):
            
            if moves == 0 and isInbound(index):
                return [1,0]
            
            if not isInbound(index):
                return [0,1]
            
            offBoard = 0
            onBoard = 0
            prob = 1/8
            
            for direction in directions:
                row = index[0] + direction[0]
                col = index[1] + direction[1]
                 
                res = explore((row, col), moves - 1)
                onBoard += res[0] * prob
                offBoard += res[1] * prob
            
            return [onBoard, offBoard]
        
  
        return explore((r, c), k)[0]