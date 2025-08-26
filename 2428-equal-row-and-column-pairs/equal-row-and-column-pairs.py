class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:

        n = len(grid)
        rows = defaultdict(int)


        for r in range(n):
            rows[','.join(str(n) for n in grid[r])] += 1
        
        print(rows)
        ans = 0

        for x in range(n):
            col = []
            for y in range(n):
                col.append(grid[y][x])

            col =  ','.join(str(n) for n in col)

            ans += rows[col]
            

        return ans