class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:


        rows = defaultdict(set)
        cols = defaultdict(set)
        box = defaultdict(set)



        for r in range(len(board)):
            for c in range(len(board[0])):
                val = board[r][c]
                if  val != ".":
                    if val in rows[r] or val in cols[c]:
                        return False

                    row = r // 3
                    col = c // 3

                    if val in box[(row,col)]:
                        return False

                    rows[r].add(val)
                    cols[c].add(val)
                    box[(row,col)].add(val)


       

        return True


            
