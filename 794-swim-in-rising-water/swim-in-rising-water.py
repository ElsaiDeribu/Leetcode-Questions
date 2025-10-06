class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:


        heap = []
        direc = [(0,1), (1,0), (0,-1),(-1,0)]
        heapq.heappush(heap, (grid[0][0],0,0))
        visited = set()
        visited.add((0,0))
        ans = grid[0][0]
        
        def inbound(r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])


        while heap:

            for _ in range(len(heap)):
                val_min, row_min, col_min = heapq.heappop(heap)

                ans = max(ans, val_min)

                for r, c in direc:
                    row_new, col_new = row_min + r, col_min + c

                    if inbound(row_new, col_new) and (row_new, col_new) not in visited:
                        heapq.heappush(heap, (grid[row_new][col_new],row_new,col_new))
                        visited.add((row_new, col_new))

                        if (row_new, col_new) == (len(grid) - 1, len(grid[0]) - 1):
                            return max(ans, grid[row_new][col_new] )




        return ans


