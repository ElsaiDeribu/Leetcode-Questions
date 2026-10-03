class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = defaultdict(set)
        cols = defaultdict(set)
        sects = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):

                if board[r][c] != ".":
                    
                    num = board[r][c]

                    R = r//3
                    C = c//3

                    if num in rows[r] or num in cols[c] or num in sects[(R,C)]:
                        return False

                    rows[r].add(num)
                    cols[c].add(num)
                    sects[(R,C)].add(num)


        return True

