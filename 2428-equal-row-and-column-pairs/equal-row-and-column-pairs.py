class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:

        rows = defaultdict(list)
        cols = defaultdict(list)

        for r in range(len(grid)):
            rows[r] = grid[r]
            for c in range(len(grid[0])):
                cols[c].append(rows[r][c])
        

        ans = 0

        for r_key in rows.keys():
            for c_key in cols.keys():
                if rows[r_key] == cols[c_key]:
                    ans += 1

        return ans