class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        
        directions = [(0,1), (1,0)]
        def isInbound(index):
            return 0 <= index[0] < len(dungeon) and 0 <= index[1] < len(dungeon[0])

        @cache
        def dp(curr):
            if curr == (len(dungeon) - 1, len(dungeon[0]) - 1):
                return min(0, dungeon[-1][-1])
            
            res = float("-inf")
            for direction in directions:
                row = curr[0] + direction[0]
                col = curr[1] + direction[1]
                
                if isInbound((row, col)):
                    res = max(res, dp((row,col)))
                    
            return min(0, res + dungeon[curr[0]][curr[1]])

        res = dp((0,0))
    
        return 1 - res
                    
                    
                    
                
            
            
        