class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        
        attackingQueens = []
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1) ]
        boardWidth = float("-inf")
        boardHeight = float("-inf")
        
        for i in range(len(queens)):
            queens[i] = tuple(queens[i])
            boardWidth = max(boardWidth, queens[i][0], king[0])
            boardHeight = max(boardHeight, queens[i][1], king[1])
            
        queens = set(queens)
        
        
        def dfs(currLocation, direction):
            
            if boardWidth < currLocation[0] or  currLocation[0] < 0 or boardHeight < currLocation[1]  or currLocation[1] < 0:
                return 
            
            x = currLocation[0] + direction[0] 
            y = currLocation[1] + direction[1]
            
            if (x, y) in queens:
                attackingQueens.append([x, y])
                return 
            
            dfs((x, y), direction)
            
            
        for direction in directions:
            dfs((king[0], king[1]), direction)
            
            
        return attackingQueens
            
        
        

        
     
            
        