class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        
        countofO = 0
        countofX = 0
        
        winComb = ["OOO", "XXX"]
        straightCount = 0
        
        for i in range(3):
            for j in range(3):
                if board[i][j] == 'O':
                    countofO += 1
                    
                elif board[i][j] == 'X':
                    countofX += 1
          
        possibleTriplets = []
        
        for row in board:
            possibleTriplets.append(row)
        
        diagonal1 = board[0][0] + board[1][1] + board[2][2]
        diagonal2 = board[0][2] + board[1][1] + board[2][0]
        
        possibleTriplets.append(diagonal1)
        possibleTriplets.append(diagonal2)
        
        
        for col in range(3):
            c = ''
            for row in range(3):
                c += board[row][col]
            possibleTriplets.append(c)
            
                
        for item in possibleTriplets:
            if item == "OOO" and countofX != countofO:
                return False
            
            if item == "XXX" and countofX != countofO + 1:
                return False
                
        
        if countofO > countofX  or countofX > countofO + 1:
            return False
                    
        
        return True
        
                    
                    
                    
