class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        

        def check(row, col):

            nums = set()

            for r in range(row - 1, row + 2):
                for c in range(col - 1, col + 2):
                    if not board[r][c] == "." and board[r][c] in nums:
                        return False

                    nums.add(board[r][c])

            return True

        cols = defaultdict(set)
        rows = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])): 
                num = board[r][c]
                if not num == ".":
                    if (num in cols[c]) or (num in rows[r]):
                        print(num, cols, rows)

                        return False

                    cols[c].add(num)
                    rows[r].add(num)

        for r in range(1,9,3):
            for c in range(1,9,3):
                if not check(r, c):
                    return False

        return True

