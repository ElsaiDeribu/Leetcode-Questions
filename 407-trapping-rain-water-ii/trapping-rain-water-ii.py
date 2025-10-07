class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        
        m, n = len(heightMap), len(heightMap[0])
        direc = [(0,1), (1,0), (-1,0), (0,-1)]
        visited = set()
        heap = []
        ans = 0

        def is_inbound(row, col):
            return 0 <= row < m and 0 <= col < n

        for r in range(m):
            for c in [0, n-1]:
                heapq.heappush(heap, (heightMap[r][c], r, c))
                visited.add((r,c))

        for c in range(n):
            for r in [0, m-1]:
                heapq.heappush(heap, (heightMap[r][c], r, c))
                visited.add((r,c))


        while heap:

            val, row, col = heapq.heappop(heap)

            for r, c in direc:

                row_new, col_new = r + row, c + col

                if (row_new, col_new) not in visited and is_inbound(row_new, col_new):

                    ans += max(0, val - heightMap[row_new][col_new])

                    heapq.heappush(heap,(max(heightMap[row_new][col_new], val), row_new, col_new))

                    visited.add((row_new, col_new))

        return ans


            





