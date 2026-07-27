class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        dirs = [(0,1), (1,0), (-1,0), (0,-1)]
        visited = set()
        def is_inbound(row, col):
            return 0 <= row < len(board) and 0 <= col < len(board[0])

        
        def visit(row, col):
            
            visited.add((row, col))
            
            for dr, dc in dirs:
                new_row = dr + row
                new_col = dc + col

                if is_inbound(new_row, new_col) and board[new_row][new_col] == "O" and (new_row, new_col) not in visited:
                    visit(new_row, new_col)
                    

        for row in [0, len(board) - 1]:
            for col in range(len(board[0])):
                if board[row][col] == "O":
                    visit(row, col)


        for row in range(len(board)):
            for col in [0, len(board[0]) - 1]:
                if board[row][col] == "O":
                    visit(row, col)


        def capture(row, col):

            board[row][col] = "X"

            for dr, dc in dirs:
                new_row = dr + row
                new_col = dc + col

                if is_inbound(new_row, new_col) and board[new_row][new_col] == "O" :
                    capture(new_row, new_col)


        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == "O" and (row, col) not in visited:
                    capture(row, col)



