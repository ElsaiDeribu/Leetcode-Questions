class Solution:
    def knightDialer(self, n: int) -> int:
        
        
        numPad = [[1,2,3],[4,5,6],[7,8,9],["*",0,"#"]]
        directions = [(-1,-2),(-1,2),(1,-2),(1,2),(-2,-1),(-2,1),(2,-1),(2,1)]
        
        def isInbound(index):
            row, col = index
            if row == 3:
                if col in [0, 2]:
                    return False
                
            return 0 <= row < len(numPad) and 0 <= col < len(numPad[0])
        
        @cache
        def dp(length, index):
            
            if length == 1:
                return 1
            
            res = 0
            for direction in directions:
                row = index[0] + direction[0]
                col = index[1] + direction[1]
                
                if isInbound((row, col)):
                    res += dp(length - 1, (row, col))
                
            return res
        
        ans = 0
        for i in range(len(numPad)):
            for j in range(len(numPad[0])):
                if isInbound((i,j)):
                    ans += dp(n, (i, j))
                    
        return ans % (10**9 + 7)
                
            
        
            
        