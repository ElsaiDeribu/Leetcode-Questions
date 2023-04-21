class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        def isInbound(index):
            row = index[0]
            col = index[1]
            
            return 0 <= row < len(board) and 0 <= col < len(board[0])
        
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        
        
        flip = 1
        iToFlip = []
        
        visited = set()
        
        
        def dfs(index):
            nonlocal flip
            
            visited.add(index)
            
            for direction in directions:
                row = direction[0] + index[0]
                col = direction[1] + index[1]
                
                if isInbound((row, col)) and board[row][col] == "O" and (row, col) not in visited:
                    dfs((row, col))
                    
                elif not isInbound((row, col)):
                    flip = 0
         
        
        def flipFun(val):
            for index in visited:
                board[index[0]][index[1]] = val
        
        
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == "O":
                    dfs((row, col))
                    
                    if flip:
                        flipFun("X")
                    else:
                        flipFun("1")
                        flip = 1   
                        
                    visited = set()

                    
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == "1":
                    board[row][col] = "O"
                    
                    
                    