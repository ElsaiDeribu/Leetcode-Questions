class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
       
            rows = [set() for _ in range(9)]
            cols = [set() for _ in range(9)]
            brd = [set() for _ in range(9)]


            for r in range(9):
                for c in range(9):
                    num = board[r][c]

                    if num == ".":
                        continue

                    brd_idx = (r // 3) * 3 + (c // 3)

                    if num in rows[r] or num in cols[c] or num in brd[brd_idx]:
                        return False

                    rows[r].add(num)
                    cols[c].add(num)
                    brd[brd_idx].add(num)
            
            return True