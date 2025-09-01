class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        dir = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,1),(1,-1),(-1,-1)]

        def isinbound(r, c):
            return 0 <= r < len(board) and 0 <= c < len(board[0])

        updates = []
        for r in range(len(board)):
            for c in range(len(board[0])):
                cnt = 0

                for d_r, d_c in dir:
                    row, col = r + d_r, c + d_c

                    if isinbound(row, col):
                        if board[row][col] == 1:
                            cnt += 1

                if board[r][c] == 1:
                    if cnt < 2 or cnt > 3 :
                        updates.append((r,c,0))

                else:
                    if cnt == 3:
                        updates.append((r,c,1))

        for r, c, v in updates:
            board[r][c] = v






        