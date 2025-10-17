class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        box = defaultdict(set)


        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] != ".":
                    if board[r][c] in rows[r] or board[r][c] in cols[c]:
                        return False

                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])


        for r in range(1, len(board), 3):
            for c in range(1, len(board[0]), 3):

                for dr in range(-1, 2):
                    for dc in range(-1, 2):
                        row = dr + r
                        col = dc + c

                        if board[row][col] != ".":

                            if board[row][col] in box[(r,c)]:
                                return False

                            box[(r,c)].add(board[row][col])


        return True


            
