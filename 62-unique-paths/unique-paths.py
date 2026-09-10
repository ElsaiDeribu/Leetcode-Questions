class Solution:
    def uniquePaths(self, m: int, n: int) -> int:


        dirs = [(0,1), (1,0)]
        def is_inbound(row, col):
            return 0 <= row < m and 0 <= col < n

        @cache
        def dfs(row, col):

            if row == m - 1 and col == n - 1:
                return 1

            if not is_inbound(row, col):
                return 0

            res = 0
            for dr, dc in dirs:
                new_row, new_col = row + dr, col + dc
                res += dfs(new_row, new_col)

            return res

        return dfs(0, 0)


        

        
        