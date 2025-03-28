class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:

        grid = [["" for _ in range(len(strs))] for _ in range(len(strs[0]))]

        for r in range(len(strs)):
            for c in range(len(strs[r])):
                grid[c][r] = strs[r][c]

        count = 0

        for row in grid:
            if not row == sorted(row):
                count += 1

        return count



        